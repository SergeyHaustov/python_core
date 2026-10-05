class ATM:
    def __init__(self, banknotes20, banknotes50, banknotes100):
        self.banknotes20 = banknotes20
        self.banknotes50 = banknotes50
        self.banknotes100 = banknotes100

    def add_money(self, banknotes20=0, banknotes50=0, banknotes100=0):
        self.banknotes20 += banknotes20
        self.banknotes50 += banknotes50
        self.banknotes100 += banknotes100

    def withdraw(self, amount):
        if amount % 10 == 0 and amount <= self.banknotes20 * 20 + self.banknotes50 * 50 + self.banknotes100 * 100:
            for count100 in range(min(amount // 100, self.banknotes100), -1, -1):
                remaining = amount - count100 * 100

                for count50 in range(min(remaining // 50, self.banknotes50), -1, -1):
                    rest = remaining - count50 * 50

                    if rest % 20 != 0:
                        continue

                    count20 = rest // 20

                    if count20 > self.banknotes20:
                        continue

                    self.banknotes100 -= count100
                    self.banknotes50 -= count50
                    self.banknotes20 -= count20

                    print(f"Выдано: 100 — {count100}, 50 — {count50}, 20 — {count20}")
                    return True
            return False
        else:
            return False


cash = ATM(8, 13, 25)
cash.add_money(1, 2, 3)
cash.withdraw(160)
cash.withdraw(1350)
cash.withdraw(1350)
cash.withdraw(200)
