class Atm(object):
	def __init__(self, cardNumber, pin):
		self.cardNumber = input("Enter card number: ")
		self.pin = input("Enter pin: ")

	def CashWithdrawl(self):
		print("Withdrawn")
	def BalanceEnquiry(self):
		print("Balance is 0")

atm1 = Atm("1234567890", "1234")
print(atm1.CashWithdrawl())
print(atm1.BalanceEnquiry)