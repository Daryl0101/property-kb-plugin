---
name: affordability
description: Estimate what a Malaysian buyer can afford and pay upfront - loan, monthly instalment, debt service ratio, down payment, stamp duty - with exact arithmetic. Use when an agent asks about a client's budget from their income, the monthly instalment, the loan amount, or the upfront costs of buying.
---

# Affordability

Property KB's tools hold project facts, not lending rules; the rules are here and the
arithmetic is in `scripts/affordability.py` (run it when you can run code; otherwise work
carefully by hand and say the figures are rounded).

## Rules (dated; they change with Budgets and bank policy)

| Rule | Value | Status |
|---|---|---|
| Loan margin, 1st and 2nd housing loan | up to 90% of the price (bank decides) | typical |
| Loan margin, 3rd housing loan onwards | at most 70% (Bank Negara) | since 2010 |
| Tenure | up to 35 years, ending by about age 70 | bank practice |
| Debt service ratio (DSR) | total monthly commitments ÷ net income; banks accept roughly 60–70%, lower for low incomes | bank practice |
| Interest rate for estimates | ask the agent, or use the panel bank's current rate; say which | changes |
| Stamp duty on the transfer | 1% first RM100k, 2% to RM500k, 3% to RM1m, 4% above | from 2019 |
| Stamp duty on the loan agreement | 0.5% of the loan | long-standing |
| Legal fees | Solicitors' Remuneration Order scale: ask the lawyer or check the current scale | do not guess |
| Exemptions (first-time buyers, affordable schemes) | change with each Budget | check the current Budget |

Also check the project's own offers first: many developers absorb legal fees or loan stamp
duty (`get` with `include=["pricing"]`), which changes the upfront cost.

## How

- **Budget from income**: `{"what": "max_price", "net_income", "commitments", "dsr_pct",
  "rate_pct", "years", "margin_pct"}`. Then `client-matching` with that `price_max`.
- **Monthly instalment**: `{"what": "instalment", "loan", "rate_pct", "years"}`. The loan is
  based on the SPA price after discounts, not the nett price after rebates.
- **Upfront costs**: `{"what": "upfront", "price", "margin_pct"}`: down payment, both stamp
  duties; legal fees and exemptions still to add.

## Answer

Show the working and the assumptions (rate, tenure, DSR, margin) and say this is an estimate:
the bank's approval decides. Never promise a loan will be approved.
