# Let us use some int value as input
num1 = 23
num2 = 32
def num_funtion():
    print(num1+num2)

num_funtion()

# input() is a function which allows for user input in the console
num3 = input("Number 3: ")
num4 = input("Number 4: ")

def addition():
    print(num3+num4)

addition()
# input() always returns a string. so, addition is not done arithmetically


# If we want a numeric type, then you need to convert the string to the appropriate type with the built-in int(), float(), or complex() function
# We have to use Type casting like below

num5 = int(input("Number 5: "))
num6 = int(input("Number 6: "))

def sum():
    print(num5+num6)

sum()