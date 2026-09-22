import pytest

from app import postal


@pytest.mark.parametrize("raw,expected", [
    ("94107", "94107"),
    ("94107-1234", "94107"),
    (" 941071234 ", "94107"),
    ("10001 - 0042", "10001"),
])
def test_normalize_zip_plus_four(raw, expected):
    assert postal.normalize(raw) == expected


def test_zone_prefix_accepts_zip_plus_four():
    assert postal.zone_prefix("US", "94107-1234") == "941"
