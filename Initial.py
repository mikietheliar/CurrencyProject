class Wallet:
    def __init__(self, usd: str, rur: str, eu: str, gbp: str, cad: str) -> None:
        self.currencies = dict()
        self.currencies['usd'] = usd
        self.currencies['rur'] = rur
        self.currencies['eu'] = eu
        self.currencies['gbp'] = gbp
        self.currencies['cad'] = cad
        self.rates = dict()
        self.rates['usd'] = {'usd': 1, 'rur': 0.011, 'eu': 1.1, 'gbp': 1.2, 'cad': 0.7}
        self.rates['rur'] = {'usd': 90, 'rur': 1, 'eu': 100, 'gbp': 120, 'cad': 60}
        self.rates['eu'] = {'usd': 0.95, 'rur': 0.01, 'eu': 1, 'gbp': 1.15, 'cad': 0.6}
        self.rates['gbp'] = {'usd': 0.7, 'rur': 0.008, 'eu': 0.85, 'gbp': 1, 'cad': 0.5}
        self.rates['cad'] = {'usd': 1.2, 'rur': 0.016, 'eu': 1.3, 'gbp': 2, 'cad': 1}

    def __str__(self) -> str:
        return str(self.currencies)

    def buy_currency(self, currency: str, amount: int) -> None:
        self.currencies[currency] += amount

    def sell_currency(self, currency: str, amount: int) -> None:
        if self.currencies[currency] < amount:
            print('Not enough money')
        else:
            self.currencies[currency] -= amount

    def convert_currency(self, from_currency: str, to_currency: str, amount: int) -> None:
        if self.currencies[from_currency] < amount:
            print('Not enough money')
        else:
            self.currencies[to_currency] += amount * self.rates[to_currency][from_currency]
            self.currencies[from_currency] -= amount

