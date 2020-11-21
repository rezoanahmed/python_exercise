class Bank():
	def __init__(self,name,balance):
		self.name = name
		self.balance = balance
	

	def transaction(self,amount):
		self.balance = self.balance + amount
		return f'{amount} transaction successful'
	def withdraw(self,amount):
		self.balance = self.balance - amount
		return f'{amount} withdraw successful'

	def __str__(self):
		print(f'Name : {name}\nBalance: {balance}')

account = Bank('Rezoan', 5000)
print(account.withdraw(1000))
print(account)