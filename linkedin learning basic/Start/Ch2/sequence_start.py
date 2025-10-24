# LinkedIn Learning Python course by Joe Marini
# Example file for complex types

# Sequences: Lists and Tuples
# These are -- surprise -- sequences of values
mylist =[0,'two',3,3.2]

lenght=len(mylist)

print(lenght)
# to access a member of a sequence type, use []
print(mylist[2])
print(mylist[-2])

# add a list to another list
# anotherlist = ['a1','a2']

# mylist= mylist + anotherlist

# use slices to get parts of a sequence


# you can use slices to reverse a sequence

print(mylist[1:4])

print(mylist[::2])

print(mylist[:4:2])
# Tuples are like lists, but they are immutable
mytuples = (0,1,2,"three")

print (mytuples[1])

# Sets are also sequences, but they contain unique values



# Set, however, can not be indexed like lists or tuples
# print(myset[0]) # this will cause an error

# Test for membership
