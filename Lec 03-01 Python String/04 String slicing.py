# [] called square bracket
# <> called angular bracket
# The first character has index number 0
# Specify the start index and the end index, separated by a colon ---> to return a part (slice) of the string. Note: The first character has index 0 and end index is not included.
x = "Pack my box with five dozen liquor jugs"
print(len(x))
print(x[2:10])

print(x[0:39]) # Why we got the whole String? Because it is counting from 0 to 38 = total 39 character

print("--------------------------------------")
print(x[:10]) # This represent start from 0, and end index is excluded
print(x[5:]) # This represent start index 5, end index is last index which is not included

print(x[0:60]) # although we know, the length is 39, we wrote 60

print("--------------------------------------")
# During Negative indexing, last index: -1
# first index always: 0
# We can use negative indexes to start the slice from the end of the string
x = "Pack my box with five dozen liquor jugs"
print(x[-10:-1])  # last index excluded#


# String slicing is very important
