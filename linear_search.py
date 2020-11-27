# First DS Program
# Linear Search
# Linear search searches in an unsorted list and one by one
mylist = [12,32,67,87,21,23,65,76,98,100,78,56,45,34,23,12,54,56,65,90]
print('Your list is : ', mylist)
search_item = int(input('Enter the item to search: '))
# mylist = list(input('Enter a list : '))


length = len(mylist)
# print(length)
for i in range(length):
	if mylist[i]==search_item:
		print('Done. The index is',mylist.index(search_item))
		break
else:
	print('Not available')