import pytest

from app import postal, zones


@pytest.mark.parametrize("code,zone", [
    ("10001", "US-NE"),
    ("30303", "US-SE"),
    ("94107", "US-W"),
])
def test_us_zone_lookup(code, zone):
    assert zones.zone_for("US", postal.zone_prefix("US", code)) == zone


def test_ca_zone_table():
    assert zones.zone_for("CA", "K1A") == "CA-ON"
    assert zones.zone_for("CA", "V6B") == "CA-BC"


def test_unknown_zone():
    with pytest.raises(zones.UnknownZone):
        zones.zone_for("US", "999")


def test_invalid_postal_code():
    with pytest.raises(postal.InvalidPostalCode):
        postal.zone_prefix("US", "1234")
