from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from app import carriers, postal, zones

app = FastAPI(title="shipping-quote-service")


class QuoteRequest(BaseModel):
    country: str = Field(min_length=2, max_length=2)
    postal_code: str
    weight_kg: float = Field(gt=0, le=70)


@app.get("/healthz")
def healthz():
    return {"status": "ok"}


@app.post("/quote")
def quote(req: QuoteRequest):
    country = req.country.upper()
    try:
        prefix = postal.zone_prefix(country, req.postal_code)
        zone = zones.zone_for(country, prefix)
    except postal.InvalidPostalCode:
        raise HTTPException(status_code=422, detail="invalid postal code")
    except zones.UnknownZone:
        raise HTTPException(status_code=422, detail="unknown shipping zone")
    rates = carriers.get_rates(zone, req.weight_kg)
    currency = "CAD" if country == "CA" else "USD"
    return {"zone": zone, "currency": currency, "rates": rates}
