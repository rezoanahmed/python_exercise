class Bank():
	def __init__(self,name,balance):
		self.name = name
		self.balance = balance
	

	def transaction(self,amount):
		self.balance = self.balance + amount
		return f'{amount} transaction successful'
	def withdraw(self,amount):
		if self.balance>=amount:
			self.balance = self.balance - amount
			return f'{amount} withdraw successful'
		else:
			return 'You do not have enough balance'

	def __str__(self):
		return f'Name : {self.name}\nBalance: {self.balance}'

account = Bank('Rezoan', 5000)
print(account)

# print(account)
print(account.transaction(10000))
print(account)
print(account.withdraw(1000))
print(account)