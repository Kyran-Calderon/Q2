class Bill:
    amount = 0
    def __init__(self, amount):
        self.amount = amount
    def pay(self, payment):
        self.amount -= payment.amount
        print("Payment made using", payment.mode)
        print("Balance:", self.amount)

class Payment:
    amount = 0
    mode = "cash"
    def __init__(self, amount):
        self.amount = amount

class Ewallet(Payment):
    def __init__(self, name, amount):
        self.mode = name
        self.amount = amount

bigBeautifulBill = Bill(100)
bayad = Payment(67)
bigBeautifulBill.pay(bayad)
gcash = Ewallet("Pisaycash", 33)
bigBeautifulBill.pay(gcash)
