"""Postal code parsing for zone lookup."""

import re

US_ZIP = re.compile(r"^\d{5}$")


class InvalidPostalCode(ValueError):
    pass


def normalize(code):
    """Drop spaces, dashes and any ZIP+4 extension, e.g. "94107-1234" -> "94107"."""
    value = re.sub(r"\D", "", code)
    return value[:5]


def zone_prefix(country, code):
    value = normalize(code)
    if country == "US" and not US_ZIP.match(value):
        raise InvalidPostalCode(code)
    return value[:3]
