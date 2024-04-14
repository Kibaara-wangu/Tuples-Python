TupleA =("Jane","Mary","John","Anna","Esther","Kibaara")
# Accessing items in a tuple
print (TupleA[2])

print(TupleA[0:3])

print(TupleA[2:-2])

print(TupleA[-3: ])

# length of a tuple
print(len(TupleA))



# Joining tuples
TupleB = ("Mango","Pineapple","Paw paw","Apple")
Tuplec = TupleA + TupleB
print(Tuplec)


# Remove items in a tuple
# change into a list first
names = list(Tuplec)
print(names)

print(names.pop())

print(names)

# Adding 1 item
names.append("Joshua")
print(names)

# Adding 2 items
names.extend(["Deborah","Sharon"])
print(names)