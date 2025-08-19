class Money:
    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        return f"Money(amount = {self.amount}, ower"

    def __eq__(self, other):
        if self.amount == other.amount:
            return True
        return False

money_igor = Money(100)
money_syimyk = Money(200)

print(money_igor)
print(f'Syimyk money is equal to Igor money \ {money_syimyk == money_igor}')