# library function, which came from Python library 
# print() to print the outcome 
# len() to know the length of String
# type() to know the type of variable

print("Hello")
print(len("Hello"))
print(type("Hello"))

print("--------------------------------------")
# User defined function
# simple One
# we use def, which represent defined; then we give a function name [any name]
# line 16 has a space/tab, which is indentation for function which define, line 16 is inside the function
def myFunction():
    print("This is my first user defined function")
    print("Good Evening")
# inside function, indentation is must

myFunction()

print("--------------------------------------")
# By using variables
empName = "Alex Wu"
empId = 352
empSalary = 5568346.563
fullTimeEmployee = True

def empInfo():
    print(empName)
    print(empId)
    print(empSalary)
    print(fullTimeEmployee)

empInfo()

print("--------------------------------------")
# By using formatted Text
# \n create new line
def emp_info():
    x = f"Employee Name: {empName.upper()} \nEmployee Id: {empId} \nEmployee Salary: {empSalary:,.4f} \nFull Time Employee: {fullTimeEmployee}"
    print(x)

emp_info()

print("---------------  Important interview question -----------------------")
# The pass Statement inside empty function
# function definitions cannot be empty, but if you for some reason have a function definition with no content, put the "pass" statement to avoid getting an error.
def my_function():
    pass
# having an empty function definition like this, would raise an error without the pass statement

my_function()