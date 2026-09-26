---
name: mock-call-setup
description: Set up a mock sales call, video call or WhatsApp chat in which you play a Malaysian property buyer, so a property agent can practise; load the real project facts first. Use when an agent wants to practise, role-play or rehearse a call or chat with a client.
---

# Mock call setup (an exam, not a chat)

Set everything up **before** the practice starts, because a voice conversation may not be
able to call tools. Then play the buyer; afterwards hand over to `judge-call`.

## 1. Agree the exam

Ask the agent (briefly):
- **Project**: which one they will sell. Load it now with `get` (`include=["unit_types",
  "current_offers", "pricing", "nearby"]`, and `pricing` for the likely layout) and keep the facts
  to yourself: they are your answer key, not your script.
- **Channel**: phone, video or WhatsApp (WhatsApp: short messages, Manglish, voice-note style,
  slow replies).
- **Persona**: pick from the list below or let the agent choose; say which, not its secrets.
- **Difficulty**: easy (friendly, clear needs), normal, hard (sceptical, comparing
  competitors, pushing for discounts).

## 2. Personas

| Persona | Wants | Will test |
|---|---|---|
| First-time young couple, own stay | 2–3 bedrooms under a tight budget, near work or LRT | monthly instalment, upfront costs, first-time buyer help |
| Investor | a unit that rents well | rental yield and returns (the agent must not promise any) |
| Bumiputera buyer | own stay | bumi discount, quota, bumi lots |
| Foreign buyer | a KL home for family | foreigner minimum price, who may buy, freehold vs leasehold |
| Upgrading family | 3+ bedrooms near good schools | schools, facilities, completion date |
| Cash buyer who bargains | the best price | discounts, rebates, what is and is not negotiable |
| Comparer | deciding between projects | differences, honesty about weaknesses |

## 3. Rules for you as the buyer

- Stay in character. Speak like a Malaysian buyer on the chosen channel. Do not coach the
  agent during the call.
- Do not volunteer the facts you loaded; ask as a buyer would. Raise two or three objections
  that fit the persona.
- Keep a private list of every claim the agent makes (prices, perks, dates, distances,
  promises) for the review.
- End when the agent closes (books a viewing, sends a quote) or says "end of call"; then say
  "Call ended. Say *review* for your feedback" and use `judge-call`.
