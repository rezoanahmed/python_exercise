# Tuples
# Tuple is not iterable that means we can't add or remove items from the tuples
mytuple = (1,2,3,4,4,5,6)
print(mytuple, type(mytuple))

for i in mytuple:
	print(i)

# We can't update tuples
# If we want to add/remove/update any items, we should convert tuples to a list and then do the rest
