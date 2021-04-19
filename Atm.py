import os

balance = 10000

try:
    CardNo = int(input("Please Enter your card Number\n"))
    Pin = int(input("\nPlease Enter your Pin\n"))

except ValueError:
    print("Please Enter a number")

while True:
    try:
        Operation = input(
            "\nWhat do you want to do??\ni)   Cash-Withdrawl\t Enter 1\nii)  Balance Enquiry\t Enter 2\niii) Change Pin\t Enter 3"+"\n\n")

    except ValueError:
        print("Please Enter a number")
        input()
        break

    if Operation == "1":
        amount = int(
            input("\nHow Much Money Do you want to Withdrawl??\n Rs:\t"))

    class Atm:
        def __init__(self, bank, pin):
            self.Bank = bank
            self.cardNo = CardNo
            self.pin = pin
            self.Balance = balance
            self.Amount = 0

        def CashWithdrawl(self):
            self.Amount = amount
            printAmount = str(self.Amount)
            cardNo = str(self.cardNo)
            self.Balance = self.Balance-amount
            if self.Balance > 0:
                AvailableBalance = str(self.Balance)
                print("\n\n"+printAmount +
                      " Rs has been WithDrawl from Card Number: " + cardNo)
                print("Available Balance: "+AvailableBalance)

            else:
                self.Balance = self.Balance + amount
                print("\nSorry... You don't have enough balance")

            ans = input("\n\nexit  y/n\t")
            if ans != "n":
                exit()
            else:
                os.system("CLS")
                return self.Balance

        def BalanceEnquiry(self):
            balance = str(self.Balance)
            print("\nBalance : Rs "+balance)

            ans = input("\n\nexit  y/n\t")
            if ans != "n":
                exit()
            else:
                os.system("CLS")

        def ChangePin(self):
            oldPin = self.pin
            newPin = int(input("Please Enter Your New Pin\n"))

            self.pin = newPin
            print("\nYour Pin Number Has Changed")

            ans = input("\n\nexit  y/n\t")
            if ans != "n":
                exit()
            else:
                os.system("CLS")
                return self.Balance

    Jhon = Atm("State Bank of India", Pin)

    if __name__ == "__main__":
        if Operation == "1":
            print(Jhon.CashWithdrawl())

        elif Operation == "2":
            print(Jhon.BalanceEnquiry())

        elif Operation == "3":
            print(Jhon.ChangePin())
