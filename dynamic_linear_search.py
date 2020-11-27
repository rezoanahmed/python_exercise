# Take a list as an input and then search the item

# Taking a list as an input
mylist = []
num = int(input('How many items do you want to add to your list?\n'))
for i in range(num):
	items = input()
	mylist.append(items)
print('Your list :',mylist)

# Linear search
search_item = input('Enter the item you want to search : ')
length = len(mylist)
insex = mylist.index(search_item)
for i in range(length):
	if mylist[i] == search_item:
		print('Yes it is available. The index is', insex)
		break
else:
	print(f'{search_item} is not available. Try again')