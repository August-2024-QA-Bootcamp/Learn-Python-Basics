name = "Mohammad Sharkar"
age = 120
grade = 3.554
usCitizen = False

print("--------------------------------------------------")
# naming convention of variable
# we can assign a value for a variable by a single letter
# under score [_] is the only symbol accepted as variable name
x = "Tofael"
y = 483
_ = 4.00

# it is very common to see underscore with other word as a variable name [LIKE BELOW ONE]
_name_ = "MTKS"

# Practice it
# windows user: shift + alt + down/up arrow to copy a line
# Mac user: shift + alt/opt + down/up arrow to copy a line

print(x)
print(y)
print(_)

# Practice it
# windows user: shift + control + k to delete a line
# Mac user: shift + command + k to delete a line
# How to reverse: control/command + z

print("--------------------------------------------------")
# Variables are case sensitive, myNAME and MYname is not same
myNAME = "Alex"
MYname = "Joe"
print(name)
print(myNAME)
print(MYname)

# alpha-numeric characters means alphabet and number both allowed together
# A variable name cannot start with a number, 1 = "Donald", 1var = "Bush"
# They are not accepted
# But number can be used in the middle or t the end
name1 = "Biden"
var1var = 435
print(name1)
print(var1var)

# What happen if variable name is same?
name = "Michael"
name = "Obama"
name = "Max"
print(name)
# python is a interpreted language
# menas covert source code to binary code line by line, 
# last statement will be executed

# Another example
y = 510 # int type
y = "Bill" # str type
print(y)
print(type(y))

# How to write Multi Words Variable Names. Can you use space between words? Ans: No
# Generally variable name start with lower case, but this is not a rule, but we will follow this
# CamelCase , Snake case and pascal case

# Example of camel case -- myName [feature start from second word]
myName = "Mohammad Sharkar"
myAge = 234
myGradeScore = 3.01

# Example of snake case -- my_name [feature start from second word]
# second word start with underscore [not semicolon, common mistake], then all lower case
my_name = "Boris"
my_age = 21
my_grade_score = 3.99

# Example of pascal case -- MyName [words start with upper case, everywhere]
MyName = "Michael"
MyAge = 67
MyGradeScore = 4.0

# Camelcase and snake-case is most popular and used in the industry, we will follow
