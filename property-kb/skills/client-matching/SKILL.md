---
name: client-matching
description: Shortlist Malaysian new property projects for a client's profile (budget, location, own stay or investment, size, family, buyer group) with Property KB. Use when an agent describes a client or asks what to offer, recommend or shortlist.
---

# Matching a client to projects

## 1. Get the profile (ask only what is missing)

| Need | Why it matters | Becomes |
|---|---|---|
| Budget (SPA price or monthly) | the hard ceiling | `price_max` (monthly: use the `affordability` skill first) |
| Where (areas, or near work/school/LRT) | commute, schools | `area`, or `near_category` + `near_within_m`, or `near_place` |
| Own stay or investment | layouts, tenure, facilities | soft `query` text |
| Bedrooms, size | family size | `bedrooms_min`, `built_up_min_sqft` |
| Buyer group: bumiputera, Malaysian, foreigner | quota, discounts, foreigner minimum price | `buyer_group` |
| Timing: ready soon or can wait | completed vs under construction | `development_status`, and read `vp_date` |
| Must-haves: freehold, facilities, pets, near international school | | `tenure`, soft `query` |

Hard needs are filters (they exclude). Wishes are the `query` text (it only ranks), e.g.
"quiet, good for young family, near international school".

## 2. One search call

`search` with the filters, the `query`, and `include=["current_offers"]`. A layout marked
"price not recorded" may still fit: say so, do not drop it silently. If nothing comes back,
loosen one filter at a time and say which.

## 3. Present a shortlist of 3 to 5

For each project: why it fits (the filters it met and the text it matched), the matching layouts
with SPA prices, the current perks, and what is uncertain. Quote figures exactly as given, with
their "as of" date and reference [n]. Map distances are estimates; say so.

Then offer next steps: a quote (`pricing-quote`), what's new in the project's Telegram group
(`search_sources` with the project and no query), or nearby schools and stations
(`get` with `include=["nearby:school_international"]`).

## Rules

- Never invent a project, price, perk or distance. The knowledge base covers the projects it
  holds, not the whole market; say "not in the knowledge base" when it is not.
- Investment questions about rental yield or capital growth: Property KB has no market data.
  Say so; never estimate yields or promise returns (advertising rules forbid promising rental
  income or capital gains).
- A warning on a fact or offer is a disclosure rule: tell the agent before they use it.
