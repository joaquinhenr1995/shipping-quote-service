"""Shipping zone lookup.

Zones are keyed by country and by the first three characters of the postal
code: the ZIP prefix for the US, the forward sortation area (FSA) for Canada.
"""

US_ZONES = {
    "021": "US-NE", "100": "US-NE", "191": "US-NE",
    "282": "US-SE", "303": "US-SE", "331": "US-SE",
    "481": "US-MW", "554": "US-MW", "606": "US-MW",
    "750": "US-SW", "787": "US-SW", "850": "US-SW",
    "900": "US-W", "941": "US-W", "981": "US-W",
}

CA_ZONES = {
    "K1A": "CA-ON", "L4W": "CA-ON", "M5V": "CA-ON",
    "G1R": "CA-QC", "H2X": "CA-QC",
    "V6B": "CA-BC", "V8W": "CA-BC",
    "T2P": "CA-AB", "T5J": "CA-AB",
}

TABLES = {"US": US_ZONES, "CA": CA_ZONES}


class UnknownZone(LookupError):
    pass


def zone_for(country, prefix):
    table = TABLES.get(country)
    if table is None or prefix not in table:
        raise UnknownZone(f"unknown shipping zone for {country} {prefix}")
    return table[prefix]
