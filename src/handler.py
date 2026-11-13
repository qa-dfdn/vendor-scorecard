"""Request handler for vendor-scorecard."""

def handle(event: dict) -> dict:
    kind = event.get("kind", "scan")
    return {"ok": True, "kind": kind, "service": "vendor-scorecard"}
