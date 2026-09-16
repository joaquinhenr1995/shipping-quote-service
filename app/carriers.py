"""Client for the internal carrier rates API."""

import os

import httpx

CARRIER_API_URL = os.environ.get("CARRIER_API_URL", "http://localhost:8081")
TIMEOUT_SECONDS = 3.0


def get_rates(zone, weight_kg):
    resp = httpx.get(
        f"{CARRIER_API_URL}/rates",
        params={"zone": zone, "weight_kg": weight_kg},
        timeout=TIMEOUT_SECONDS,
    )
    resp.raise_for_status()
    return [
        {"carrier": r["carrier"], "service": r["service"], "amount": round(r["amount"], 2)}
        for r in resp.json()["rates"]
    ]
