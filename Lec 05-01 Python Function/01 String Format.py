fname = "Mohammad"
lname = "Sharkar"
age = 100
salary = 8476587643

print(fname, lname, age)
print("First Name:", fname, "Last Name:", lname, "Age:", age)
# TypeError: can only concatenate str (not "int") to str
# print("First Name:" + fname + "Last Name:" + lname + "Age:" + age)

# formatted text
# by formatting text, we can get a outcome of String and other data type together
# this {} is called placeholder
outcome1 = f"First Name: {fname}, Last Name: {lname}, Age: {age}"
print(outcome1)

# We can manipulate formatted Text by calling different method
# {salary:,.3f} will provide 3 value after decimal and comma for each thousand
outcome2 = f"First Name: {fname.upper()}, Last Name: {lname.lower()}, Age: {age}yr, Salary: {salary:,.3f}$"
print(outcome2)

cost1 = 4.1
print(f"Fuel price {cost1:.2f}$")

cost2 = 5.02
total1 = f"Gas price {cost2:.3f}$"
print(total1)

cost3 = 6
total2 = f"Gas price {cost1*cost2+cost3}$"
print(total2)

# Another example
# {} is called placeholder, which hold the variable
# we can call string methods inside it, line 18
# We can do arithmetic function inside placeholder. line 29 
# example: price + (price*tax)
# We can Display the price with 2 or 3 decimals, line 22, 25
# formatted text can be present inside single quotation too
# We can use a comma as a thousand separator
product = "goLD flAMe"
price = 453765
tax = 0.10

x = f'The price of {product.title()} is {price + (price*tax):.3f}'
print(x)
# {price + (price*tax):.3f} did not give comma, so thousands separator is absent

# If we wanna use " " around a name, can we use it inside formatting text? How?
y = f"The price of \"{product.title()}\" is {price + (price*tax):,.3f}"
print(y)

# we can also use \n, \t



