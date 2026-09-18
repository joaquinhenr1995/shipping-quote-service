from fastapi.testclient import TestClient

from app import carriers
from app.main import app

client = TestClient(app)


def fake_rates(zone, weight_kg):
    return [{"carrier": "acme", "service": "ground", "amount": 9.5}]


def test_quote_us(monkeypatch):
    monkeypatch.setattr(carriers, "get_rates", fake_rates)
    resp = client.post("/quote", json={"country": "US", "postal_code": "10001", "weight_kg": 2})
    assert resp.status_code == 200
    assert resp.json()["zone"] == "US-NE"
    assert resp.json()["currency"] == "USD"


def test_quote_unknown_zone():
    resp = client.post("/quote", json={"country": "US", "postal_code": "99999", "weight_kg": 1})
    assert resp.status_code == 422
    assert resp.json()["detail"] == "unknown shipping zone"
