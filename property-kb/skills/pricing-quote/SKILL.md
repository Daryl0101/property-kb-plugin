---
name: pricing-quote
description: Work out what a buyer actually pays for a Malaysian new property unit or layout (SPA price, discounts, rebates, bumi discount, packages) with Property KB, and explain it. Use when an agent asks for a price, nett price, quote, discount, rebate or "how much after promotion".
---

# A correct price quote

The tools do the arithmetic; you decide which offers apply. Offer terms are messy text and the
plan is your judgement.

## Steps

1. **Find the layout or unit**: `search` or `get` by name with the project.
2. **Get the pricing facts**: `get` with `include=["pricing"]`. You receive the SPA prices
   (dated), every current buyer offer with its exact terms, eligibility, printed basis
   (`calculated_on`) and recorded conflicts (`not_combinable_with`), agent-side offers apart,
   and a suggested plan labelled as an assumption.
3. **Ask the buyer group** if you do not know it: bumiputera, Malaysian, foreigner; first-time
   buyer; cash or loan; repeat buyer. Several offers depend on it.
4. **Decide the plan.** Read every offer's terms. Leave out what the buyer cannot take
   (group, "first 50 buyers" already gone, "not applicable with DIBS" when they chose DIBS, a
   package they declined). Order and basis:
   - use the printed basis when there is one ("7% on the nett price" means after the others);
   - otherwise the usual convention: discounts come off the SPA price first, rebates are worked
     out on the discounted price. Say it is an assumption.
5. **Calculate**: `calculate_price` with the target, `buyer_group` and your steps
   (`{offer, on: "spa" | "running"}`; your own adjustments as `{label, amount | pct}`, negative
   lowers). Read every warning it returns.
6. **Answer** with the breakdown:
   - **SPA price after discounts**: what goes on the SPA and what the loan is based on;
   - **nett price after rebates**: what the buyer ends up paying (rebates and cashback are paid
     back after the SPA, often in stages: say when, from the terms);
   - non-cash perks (furnishing, fee waivers, gifts) listed, not priced;
   - the conditions, the dates of the figures, references [n], and each warning.

## Words that matter

- **Discount** lowers the SPA price. **Rebate** or **cashback** is paid back after the SPA. Use
  the source's own word (`printed_term`); never relabel one as the other.
- **Bumi discount** applies to bumiputera buyers only, usually on the SPA price.
- **Nett price** is after rebates; say which rebates.
- **Free legal fees** and similar waivers may not be advertised (a restricted disclosure
  warning): fine to tell a buyer in conversation, not to put in an ad.
- A lucky draw (`chance_based`) is never promised as part of the price.

If the terms are ambiguous, say what is ambiguous and suggest confirming with the developer:
a precise-looking number built on a guess is worse than an honest range.
