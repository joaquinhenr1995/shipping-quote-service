from typing import Optional

from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel, Field

from app import carriers, postal, zones
from app.messages import message

app = FastAPI(title="shipping-quote-service")


class QuoteRequest(BaseModel):
    country: str = Field(min_length=2, max_length=2)
    postal_code: str
    weight_kg: float = Field(gt=0, le=70)


@app.get("/healthz")
def healthz():
    return {"status": "ok"}


@app.post("/quote")
def quote(req: QuoteRequest, accept_language: Optional[str] = Header(default=None)):
    country = req.country.upper()
    try:
        prefix = postal.zone_prefix(country, req.postal_code)
        zone = zones.zone_for(country, prefix)
    except postal.InvalidPostalCode:
        raise HTTPException(status_code=422, detail=message("invalid_postal_code", accept_language))
    except zones.UnknownZone:
        raise HTTPException(status_code=422, detail=message("unknown_zone", accept_language))
    rates = carriers.get_rates(zone, req.weight_kg)
    currency = "CAD" if country == "CA" else "USD"
    return {"zone": zone, "currency": currency, "rates": rates}
