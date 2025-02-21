class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency
    
    def __add__(self, other):
        if self.currency == other.currency:
            return Money(
                self.amount + other.amount,
                self.currency
            )
        else:
            raise RuntimeError("Mismatched currencies!")
        
    def __sub__(self, other):
        if self.currency == other.currency:
            return Money(
                self.amount - other.amount,
                self.currency
            )
        else:
            raise RuntimeError("Mismatched currencies!")
        
    def __mul__(self, multiply):
        return Money(self.amount * multiply, self.currency)

# money1 = Money(15, "EUR")
# money2 = Money(30, "EUR")
# money3 = Money(60, "USD")
# money4 = Money(48, "USD")

# moneyAdd43 = money4 + money3
# moneySubstract21 = money2 - money1
# moneyMultiply45 = money4 * 5


# print(moneyAdd43.amount, moneyAdd43.currency)
# print(moneySubstract21.amount, moneySubstract21.currency)
# print(moneyMultiply45.amount, moneyMultiply45.currency) 
