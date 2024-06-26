class Wallet:
    def __init__(self, usd: str, rur: str, eu: str, gbp: str, cad: str) -> None:
        self.currencies = dict()
        self.currencies['usd'] = usd
        self.currencies['rur'] = rur
        self.currencies['eu'] = eu
        self.currencies['gbp'] = gbp
        self.currencies['cad'] = cad
        self.rates = dict()
        self.rates['usd'] = {'usd': 1, 'rur': 0.01, 'eu': 1.1, 'gbp': 1.3, 'cad': 0.7}
        self.rates['rur'] = {'usd': 90, 'rur': 1, 'eu': 100, 'gbp': 120, 'cad': 67}
        self.rates['eu'] = {'usd': 0.9, 'rur': 0.01, 'eu': 1, 'gbp': 1.2, 'cad': 0.7}
        self.rates['gbp'] = {'usd': 0.8, 'rur': 0.009, 'eu': 0.85, 'gbp': 1, 'cad': 0.6}
        self.rates['cad'] = {'usd': 1.4, 'rur': 0.015, 'eu': 1.5, 'gbp': 1.7, 'cad': 1}

    def __str__(self) -> str:
        return str(self.currencies)

    def buy_currency(self, currency: str, amount: int) -> str:
        self.currencies[currency] += amount
        return str(self.currencies)

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

    def stack(self, to_currency: str) -> int:
        stack = 0
        for currency in self.currencies:
            stack += self.currencies[to_currency] * self.rates[to_currency][currency]
        return stack

    def buy_goods_check(self, goods_currency: str, price: int) -> bool:
        if self.stack(goods_currency) >= price:
            return True
        return False

    def buy_goods(self, goods_currency: str, price: int) -> None:
        if self.buy_goods_check(goods_currency, price):
            stack = 0
            price = price * self.rates[goods_currency][goods_currency]
            for currency in self.currencies:
                stack += self.currencies[goods_currency] * self.rates[goods_currency][currency]
            if stack >= price:
                for currency in self.currencies:
                    a = self.currencies[currency] * self.rates[goods_currency][currency]
                    if a < price:
                        price -= a
                        self.currencies[currency] = 0
                    else:
                        self.currencies[currency] -= price / self.rates[goods_currency][currency]
                        break
            print(self.__str__())
        else:
            print('Not enough money')


class Person:

    def __init__(self, name: str) -> None:
        self.name = name
        self.wallet = Wallet(0, 0, 0, 0, 0)

    def __str__(self) -> str:
        return self.name + ' ' + str(self.wallet)
