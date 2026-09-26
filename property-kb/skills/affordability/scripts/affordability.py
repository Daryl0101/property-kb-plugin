#!/usr/bin/env python3
"""Exact arithmetic for Malaysian home-loan affordability (the `affordability` skill).

Standard library only. Every rate is an input with a documented default, so a changed rule is
a changed argument, not a changed script. Run with a JSON object on stdin or as an argument:

    python3 affordability.py '{"what": "instalment", "loan": 700000, "rate_pct": 4.2, "years": 35}'
    python3 affordability.py '{"what": "stamp_duty", "price": 821000}'
    python3 affordability.py '{"what": "max_price", "net_income": 9000, "commitments": 800,
                               "dsr_pct": 60, "rate_pct": 4.2, "years": 35, "margin_pct": 90}'
    python3 affordability.py '{"what": "upfront", "price": 821000, "margin_pct": 90}'

Prints one JSON object: the figures and the rules used, so the answer can show its working.
"""

from __future__ import annotations

import json
import math
import sys

MOT_TIERS = [(100_000, 1.0), (500_000, 2.0), (1_000_000, 3.0), (math.inf, 4.0)]
"""Stamp duty on the transfer (memorandum of transfer), Stamp Act 1949, from 1 Jan 2019: 1% on
the first RM100k, 2% up to RM500k, 3% up to RM1m, 4% above. Verify after each Budget."""

LOAN_STAMP_PCT = 0.5
"""Stamp duty on the loan agreement: 0.5% of the loan. Verify after each Budget."""


def instalment(loan: float, rate_pct: float, years: int) -> float:
    """Monthly repayment of an annuity loan."""
    months = years * 12
    r = rate_pct / 100 / 12
    if r == 0:
        return loan / months
    return loan * r * (1 + r) ** months / ((1 + r) ** months - 1)


def loan_for(monthly: float, rate_pct: float, years: int) -> float:
    """The loan a monthly repayment supports (the inverse of `instalment`)."""
    months = years * 12
    r = rate_pct / 100 / 12
    if r == 0:
        return monthly * months
    return monthly * ((1 + r) ** months - 1) / (r * (1 + r) ** months)


def tiered(amount: float, tiers: list[tuple[float, float]]) -> tuple[float, list[dict]]:
    """Tax on `amount` by marginal tiers [(upper bound, %)]: (total, the working)."""
    total, lower, working = 0.0, 0.0, []
    for upper, pct in tiers:
        if amount <= lower:
            break
        part = min(amount, upper) - lower
        duty = part * pct / 100
        working.append(
            {"from": lower, "to": min(amount, upper), "pct": pct, "duty": round(duty, 2)}
        )
        total += duty
        lower = upper
    return total, working


def stamp_duty(price: float, tiers=None) -> dict:
    tiers = [(math.inf if u is None else u, p) for u, p in (tiers or MOT_TIERS)]
    total, working = tiered(price, tiers)
    return {"price": price, "transfer_stamp_duty": round(total), "working": working}


def upfront(price: float, margin_pct: float, loan_stamp_pct: float = LOAN_STAMP_PCT) -> dict:
    loan = price * margin_pct / 100
    return {
        "price": price,
        "loan": round(loan),
        "down_payment": round(price - loan),
        "transfer_stamp_duty": stamp_duty(price)["transfer_stamp_duty"],
        "loan_stamp_duty": round(loan * loan_stamp_pct / 100),
        "not_included": "legal fees and disbursements (ask the lawyer or check the current "
        "Solicitors' Remuneration Order scale); any exemption the buyer qualifies for",
    }


def max_price(
    net_income: float,
    commitments: float,
    dsr_pct: float,
    rate_pct: float,
    years: int,
    margin_pct: float,
) -> dict:
    room = net_income * dsr_pct / 100 - commitments
    if room <= 0:
        return {"monthly_room": round(room), "max_loan": 0, "max_price": 0}
    loan = loan_for(room, rate_pct, years)
    return {
        "monthly_room": round(room),
        "max_loan": round(loan),
        "max_price": round(loan / (margin_pct / 100)),
        "rules": f"DSR {dsr_pct}% of net income, {rate_pct}% p.a., {years} years, "
        f"{margin_pct}% margin",
    }


def main(raw: str) -> dict:
    args = json.loads(raw)
    what = args.pop("what")
    if what == "instalment":
        monthly = instalment(args["loan"], args["rate_pct"], args["years"])
        return {
            **args,
            "monthly": round(monthly, 2),
            "total_paid": round(monthly * args["years"] * 12),
        }
    if what == "stamp_duty":
        return stamp_duty(args["price"], args.get("tiers"))
    if what == "upfront":
        return upfront(
            args["price"], args["margin_pct"], args.get("loan_stamp_pct", LOAN_STAMP_PCT)
        )
    if what == "max_price":
        return max_price(
            args["net_income"],
            args.get("commitments", 0),
            args["dsr_pct"],
            args["rate_pct"],
            args["years"],
            args["margin_pct"],
        )
    raise SystemExit(f"unknown 'what': {what}")


if __name__ == "__main__":
    text = sys.argv[1] if len(sys.argv) > 1 else sys.stdin.read()
    print(json.dumps(main(text), indent=2))
