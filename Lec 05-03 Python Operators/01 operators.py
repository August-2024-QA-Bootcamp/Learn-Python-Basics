# Operators are used to perform operations on variables and values.
# In the example below, we use the + operator to add together two values:
print(5+7)

x = 20
y = 6

# Addition
print(x+y)

# Subtraction
print(x-y)

# Multiplication
print(x*y)

# Division
print(x/y)
# The above division gave us a float number
# but if you need a solid number or int number, not a float, what you will use? see below

# Floor division [new]
print(x//y)

# Modulus or remainder
print(x%y)

# Exponentiation
a = 2
b = 3
print(a**b)

'''
The = operator is used for assignment, such as when assigning a value to a variable. The == operator is the relational operator for checking equality of two values. If the values are the same, it will return True , and will return False otherwise.
'''

print("--------------------------------------")
# Python Comparison Operators
m = 6 # here you assign a value for m
n = 4

# Equal
print(m==n) # here you compare the value

# Not Equal
print(m!=n)

# Greater than
print(m>n)

# Less than
print(m<n)

# Greater than or equal to
print(m>=n)

# Less than or equal to
print(m<=n)

print("--------------------------------------")
# Python logical operator ----> 'and', 'or', 'not'

# 'and' operator Returns True if both statements are true
x = 5
print(x > 3 and x < 10) # both statement true
print(x > 10 and x < 10) # one statement true, another one false
print(x > 10 and x < 5) # both statement false

print("--------------------------------------")
# 'or' operator Returns True if one of the statements is true
y = 5
print(y > 3 or y < 10) # both statement true
print(y > 10 or y < 10) # one statement true, another one false
print(y > 10 or y < 5) # both statement false

print("--------------------------------------")
# 'not' operator Reverse the result, returns False if the result is true
y = 5
print(not(y > 3 and y < 10)) 
print(not(y > 10 and y < 10)) 
print(not(y > 10 and y < 5))

