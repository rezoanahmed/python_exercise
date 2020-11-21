# Prime or Composite
num = 10
for i in range(2,num):
	if(num%i == 0):
		print(f'{num} is not prime')
	else:
		print(f'{num} is prime')