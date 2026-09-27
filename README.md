# Property KB plugin

Current, dated, referenced facts on Malaysian new property projects for property agents' AIs,
with skills for client matching, price quotes, affordability, mock calls and call reviews.

This repository holds only the installable plugin: manifests and skills. Using the tools needs
a Property KB account: sign in with Google when your AI asks, then wait for approval.

- Website: https://daryl0101.github.io/property-kb-plugin/
- Install instructions (written for your AI to follow): https://property-kb-plugin-64268236583.us-central1.run.app/install
- Claude Code: `claude plugin marketplace add Daryl0101/property-kb-plugin` then
  `claude plugin install property-kb@property-kb`
- Claude or ChatGPT apps: add a connector/app with the MCP address `https://property-kb-plugin-64268236583.us-central1.run.app/mcp`, and the
  folders of `property-kb/skills/` as skills where your app offers them.

## Example prompts

Once Property KB is connected, ask your AI in your own words, for example:

**Shortlist projects for a client**

> My client is a Malaysian couple buying to live in. Budget RM700k, at least 3 bedrooms, near an LRT station around Bukit Jalil or Cheras. Shortlist projects from Property KB with their current offers.

**Quote the price after offers**

> What does a non-bumi first-time buyer pay for the smallest 3-bedroom layout at The Queenswoodz after all current discounts and rebates? Show the breakdown with sources.

**Catch up on what's new**

> What's new at The Queenswoodz this week? Summarise the admins' updates with their dates, and tell me what changed since last week.

**Work out what a client can afford**

> My client earns RM9,000 a month after tax and pays RM1,200 a month for a car loan. What price can they afford at 4.2% over 35 years, and how much do they need upfront?

**Practise a sales call**

> Set up a mock WhatsApp chat. You are a sceptical bumiputera buyer looking at The Aldenz, comparing it with other projects. Hard difficulty.

**Check a real call before you follow up**

> Review this call with my client. Check every price, offer and promise I made against Property KB, then score the call and tell me what to fix: [paste the transcript or WhatsApp chat]

Generated from the Property KB code repository (`pkb plugin export`); changes made here are
overwritten.

Feedback: https://wa.link/xgiqt7
