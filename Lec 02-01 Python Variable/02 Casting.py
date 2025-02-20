print("--------------------------------------------------")
# Variables can even change type after they have been set.
x = 7 # int type
x = 3.0563 # float type
print(x)
print(type(x))

print("--------------------------------------------------")
x = 4
print(x)
print(type(x))

# What is casting, to convert one data type to another data type
# although 4 is int, but we can cast int type to a str type by str() function
y = str(4)
print(y)
print(type(y))

# like to turn to a boolean type
z = bool("Tofael")
print(z) # why the value is True, because already converted to boolean, and default value True
print(type(z))

m = int(True)
print(m) # default value of int is 1
print(type(m))

a = "4"
print(a)
print(type(a))