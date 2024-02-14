# parent/superclass

class Mpesa:
    def __init__(self, account_balance, phone_number):
        self.account_balance = account_balance
        self.phone_number = phone_number

    def send_money(self, amount, recipient):
        if self.account_balance >= amount:
            self.account_balance -= amount
            print(f"{amount} KES sent to {recipient} successfully")
        else:
            print("Insufficient balance")


# child classes 1
class PersonalMpesa(Mpesa):
    def __init__(self, account_balance, phone_number, id_number):
        super().__init__(account_balance, phone_number)
        self.id_number = id_number

    def buyairtime(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            print(f"{amount} has successfully been credited")
        else:
            print("Insufficient balance")


# child class 2
class BusinessMpesa(Mpesa):
    def __init__(self, account_balance, phone_number, business_name):
        super().__init__(account_balance, phone_number)
        self.business_name = business_name

    def receivepayment(self, amount):
        self.account_balance += amount
        print(f"{amount} KES received from a client")


# instance for personal class
Personal = PersonalMpesa(145999, 756895644, 4567646447)
Personal.send_money(10000, 10987654432)
Personal.buyairtime(4000)

# instance for business class
Business = BusinessMpesa(50000, 74536271890, "Brian")
Business.send_money(10000, "Jacky")
Business.receivepayment(30000)
