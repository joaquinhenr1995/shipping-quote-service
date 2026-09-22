"""User-facing error messages for quote validation."""

MESSAGES = {
    "en": {
        "invalid_postal_code": "invalid postal code",
        "unknown_zone": "unknown shipping zone",
    },
    "es": {
        "invalid_postal_code": "codigo postal no valido",
        "unknown_zone": "zona de envio desconocida",
    },
}


def message(key, accept_language=None):
    lang = (accept_language or "en").split(",")[0].split("-")[0].strip().lower()
    return MESSAGES.get(lang, MESSAGES["en"])[key]
