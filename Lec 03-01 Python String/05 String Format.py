fname = "Mohammad"
lname = "Sharkar"
age = 100

print(fname + lname)
# print(fname + age) # can only concatenate str to str, (not str to "int") 
print(fname, age) # this is Ok

# cannot concatenate str to "int", see below line
# print("My name: " + fname + " " + lname + ", Age" + age)

# Python Format String
fname = "Mohammad"
lname = "Sharkar"
age = 100
salary = 125000

# when we format text, first give lower case f then doule quotation,
# define variables inside curly braces
# by formatting text, we can get a outcome of String and other data type like int, together
# this {} is called placeholder

outcome = f"My Name is {fname} {lname}, my age {age} and my salary {salary}"
print(outcome)

