"""Postal code parsing for zone lookup."""

import re

US_ZIP = re.compile(r"^\d{5}$")
CA_POSTAL = re.compile(r"^[A-Z]\d[A-Z]\d[A-Z]\d$")


class InvalidPostalCode(ValueError):
    pass


def clean(code):
    return code.strip().upper().replace(" ", "")


def zone_prefix(country, code):
    value = clean(code)
    if country == "US" and US_ZIP.match(value):
        return value[:3]
    if country == "CA" and CA_POSTAL.match(value):
        return value[:3]
    raise InvalidPostalCode(code)
