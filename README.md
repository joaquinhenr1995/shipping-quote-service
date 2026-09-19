# shipping-quote-service

Returns shipping quotes for storefront checkout. Supports US and Canadian
addresses.

## Run locally

    python -m venv .venv
    . .venv/bin/activate
    pip install -r requirements.txt
    uvicorn app.main:app --reload

The service calls the carrier rates API at CARRIER_API_URL
(default http://localhost:8081).

## API

POST /quote

    {"country": "CA", "postal_code": "K1A 0B1", "weight_kg": 1.5}

Returns the shipping zone, the currency and one rate per carrier service.
Errors come back as 422 with "invalid postal code" or "unknown shipping zone".

GET /healthz returns {"status": "ok"}.

## Tests

    pytest
