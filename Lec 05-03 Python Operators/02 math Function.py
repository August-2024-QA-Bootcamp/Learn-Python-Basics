# Built in Math function

# The max() functions can be used to find the highest value in an iterable
print(max(25436, 6354, 7286, 587264, 258762))

# The min() functions can be used to find the lowest value in an iterable
print(min(25436, 6354, 7286, 587264, 258762))

# The abs() function returns the absolute (positive) value of the specified number
print(abs(-34.567364))


# Exponentiation
a = 2
b = 5
print(a**b)
# The pow(x, y) function returns the value of x to the power of y (xy).
print(pow(2,3))

# round(), Round to the nearest integer
print(round(3.2))
print(round(3.4))
print(round(3.5))
print(round(3.8))

# we are importing math library by below line
import math

# The math.sqrt() method returns the square root of a number
print(math.sqrt(64))

# floor function, Rounds a number down to the nearest integer
print(math.floor(3.7))

# ceiling function, Rounds a number up to the nearest integer
print(math.ceil(3.1))

# The math.factorial() method returns the factorial of a number. 5x4x3x2x1
print(math.factorial(5))

# below one gave us remainder or modulus
x = 20
y = 6
print(x%y)

# method returns the remainder of x with respect to y
# x = Required. The number you want to divide.
# y = Required. The number you want to divide with. It must be a non-zero number, or a ValueError occurs.

print(math.remainder(9, 2))
print(math.remainder(9, 3))
print(math.remainder(9, 4)) # why not working with 9, 5, have to find out

# we are importing date and time library
import datetime
print(datetime.datetime.now())
