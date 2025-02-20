print("--------------------------------------")
print("Hello!")
print("Welcome to Python")

print("--------------------------------------")
# 1st way: please don't use
# String Concatenation: when combine/connect 2 String
# To concatenate, or combine, two strings - we can use the + operator.
print("Hello!" + "Welcome to Python")  
# white space is not created in between --> "Hello!Welcome to Python"

print("--------------------------------------")
# solution:
# We can use coma to concatenate which provide space between String
print("Hi!", "Let's learn Python")

print("----------- Standard, you will see, high level, you must learn ---------------")
# The end parameter in the print function is used to add any string. At the end of the output of the print statement in python. By default, the print function ends with a newline. Passing the whitespace to the end parameter (end=' ') indicates that the end character has to be identified by whitespace and not a newline.
print("Hi!", "This is about Python.", end= " ")
print("I am using end feature here, it will concatenate the previous line ")

# Another example with variables
print("--------------------------------------")
firstName = "Mohammad"
lastName = "Sharkar"

print(firstName + lastName) 
print(firstName + " " + lastName) # This is not smart code
print(firstName, lastName) # we will use this
print("--------------------------------------")
print(firstName, end=" ") 
print(lastName) # we will use this

print("--------------------------------------")
# We can assign a multiline string to a variable by using three double or single quotes (not common)
a = """My Name is Alex, 
I am 200 years old,
I live in NY,
I love Python"""

print(a)
print(len(a))