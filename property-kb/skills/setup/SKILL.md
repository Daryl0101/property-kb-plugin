---
name: setup
description: Check that Property KB is installed and working, and fix what is not (sign-in, approval, subscription, missing skills). Use when the user sets up Property KB, when a Property KB tool returns an error about signing in, approval or subscription, or when they ask whether it works.
---

# Property KB setup check

Property KB has two parts: **tools** (a connector/app named Property KB, which reads the
knowledge base) and **skills** (this one, `client-matching`, `pricing-quote`, `affordability`,
`mock-call-setup`, `judge-call`, `glossary`). The tools are what matter most: without them,
nothing here can answer a property question.

## Check, in order

1. **Are the tools there?** Look for a tool named `describe` from Property KB. If there is none,
   the connector is not installed or not enabled in this chat: go to *Install*.
2. **Do they answer?** Call `describe` with no arguments.
   - It returns node types: **all good.** Say so, and list the skills you can see.
   - It returns an error. Read it to the user in plain words and follow it:

| The error says | What it means | What the user does |
|---|---|---|
| "Sign in to Property KB first" | The connector is not signed in | Reconnect Property KB in the app's connector/app settings and sign in with Google |
| "waiting for approval" | Signed up; the owner has not verified them yet | Nothing: the owner will contact them on the phone number they gave |
| "not approved" | The owner refused the account | Contact the owner |
| "approved. Subscribe…" with a link | Verified, no subscription yet | Open the link, pay, then ask the question again |
| "approved. Start your free…" with a link | Verified; a free trial is offered | Open the link and enter a card (charged only when the trial ends), then ask the question again |
| "payment did not go through" with a link | The card failed | Open the link to update payment |

Status changes apply on the very next tool call; no reconnecting needed after approval or
payment.

3. **Skills.** If some of the skills listed above are missing, the tools still carry them: call
   `guide` with a skill's name and follow what it returns. Installing the skills is optional.

## Install

The install page, written for AIs, is at `<Property KB address>/install` and on the website
(`https://daryl0101.github.io/property-kb-plugin/install/`); read it and follow it for the
user's app. In short:

- **Claude Code / Codex:** install the `property-kb` plugin (it brings the tools and all the
  skills), then sign in when the connector asks.
- **Claude app:** add Property KB as a custom connector with the MCP address
  `<Property KB address>/mcp`, sign in with Google, give your phone number once.
- **ChatGPT:** Free and Go plans cannot add it yet. Plus and Pro, on the web: Settings →
  Security and login → Developer mode on; then Settings → Plugins → + with the MCP address
  `<Property KB address>/mcp`; sign in with Google. Business: only a workspace admin can add
  it (Workspace settings → Apps → Create, then publish).
- Either app: the skills come through the `guide` tool; installing them as skills is optional
  (ChatGPT: Business, Enterprise and Edu workspaces; Claude: Settings, Skills). App menus
  change; if a name here is not on screen, look for "connectors", "plugins", "apps" or "skills".

Never ask the user for passwords, card numbers or codes: sign-in and payment happen on
Google's and Stripe's own pages.
