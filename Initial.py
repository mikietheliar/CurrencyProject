class Wallet:
    def __init__(self, usd: str, rur: str, eu: str, gbp: str, fr: str) -> None:
        self.currencies = dict()
        self.currencies['usd'] = usd
        self.currencies['rur'] = rur
        self.currencies['eu'] = eu
        self.currencies['gbp'] = gbp
        self.currencies['fr'] = fr

