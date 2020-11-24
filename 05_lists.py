# Lists
mylist = [1,2,3,4,5,6,7,8,9]
print(mylist, type(mylist))

# We can add different data types in a list
mylist2 = [1,2,3,'a','b','c',3.14, True]
print(mylist2)

# We can add list within a list
mylist3 = [1,2,[3,4],['a','b']]
print(mylist3)

# List indexing
print(mylist[0])
print(mylist[-1])
print(mylist[5:])
print(mylist[:5])
print(mylist[2:6])
print(mylist[::-1])
print(mylist3[2][1])
print(mylist3[3])

# List operations
newlist = [1,2,3]
newlist.append(4)
print(newlist)
newlist.pop()
print(newlist)
newlist.insert(0,5)
print(newlist)
newlist.sort()
print(newlist)
newlist.reverse()
print(newlist)
print(newlist.index(1))
newlist.remove(5)
print(newlist)
newlist.clear()
print(newlist)

# List Comprehension
mynewlist = [x for x in range(1,10) if x%2==0]
print(mynewlist)
