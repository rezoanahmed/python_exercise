# Sets
myset = {1,2,3,4,5,6,7,8}
print(myset, type(myset))
myset.add(9)
print(myset)
myset.remove(3)
print(myset)

# Set operations
newset = {1,11,22,33}
print(myset.union(newset))
print(myset.intersection(newset)) #Empty set will return set()
print(myset.symmetric_difference(newset))
