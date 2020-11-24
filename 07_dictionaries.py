# Dictionaries
mydict = {'Name': 'Rezoan', 'Age':21, 'Department':'CSE'}
print(mydict, type(mydict))
print(mydict['Name'])
print(mydict['Age'])

car = {
	'car': 'Lamborghini Aventador SVJ',
	'owner': 'Md Rezoan Ahmed',
	'year': 2022
}
print(car)
# print(car['car'])
car['car'] = 'Mclaren 765lt'
car['year'] = 2023
print(car)
car['color'] = 'silver'
print(car)
car.pop('color')
print(car)

# For Loop In Dictionaries
for i in car:
	print(i)

for i in car.items():
	print(i)

for i,j in car.items():
	print(i,':',j)