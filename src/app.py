"""Vendor scorecard for Mistvale Ingredients"""

class VendorScorecard:
    """Internal service for vendor-scorecard."""

    def status(self) -> str:
        return "ok"


if __name__ == "__main__":
    print(VendorScorecard().status())
