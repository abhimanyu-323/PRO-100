class ATM:
    def __init__(self,cardnumber,pin):
        self.cardnumber=cardnumber
        self.pin=pin

    def check_balance(self):
        print("Your balance is 12000")

    def withdrawl(self,amount):
        new_amount = 500 - amount
        print("withdrawn amount "+str(amount) +".Your remaining balance is "+ str(new_amount))


def main():
    Card_number = input("enter your card number:")
    pin_number  = input("enter your pin number:")

    new_user =  ATM(Card_number ,pin_number)

    print("Choose your activity ")
    print("1.Balance Enquriy   2.withdrawl")
    activity = int(input("enter account number :"))

    if (activity == 1):
        new_user.check_balance()
    elif (activity == 2):
        amount = int(input("enter the amount:"))
        new_user.withdrawl(amount)
    else:
        print("enter a valid number")


if __name__ == "__main__":
    main()