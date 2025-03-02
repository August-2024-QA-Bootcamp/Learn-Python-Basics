def myFunction():
    print("This is my first user defined function")
    print("Good Evening")

myFunction()

print("--------------------------------------")
# A parameter is the variable listed inside the parentheses of the function definition.
def empInfo(empName, empId, empSalary, fullTimeEmployee):
    x = f"Employee Name: {empName.upper()} \nEmployee Id: {empId} \nEmployee Salary: {empSalary:,.4f} \nFull Time Employee: {fullTimeEmployee}"
    print(x)

# We define [put the value] the variables when the function is called
# An argument is the value that is sent to the function when it is called.
# the order of the arguments does matter. we have to follow the entry, see line 18, also number of argument must match with numbe rof parameter
empInfo("Tanvir", 5354, 568468.653746, False)

print("--------------------------------------")
empInfo("Shami", 4324, 46546383.78, True)
# empInfo(4543, "jhfkdsh", True, 34765894793)

print("--------------------------------------")
# By default, a function must be called with the correct number of arguments. Meaning that if your function expects 4 arguments, you have to call the function with 4 arguments, not more, and not less.
empInfo("Aysha", 6352, 834827638, False)
# The advantage of function with parameter is --> we can reuse that function with different arguments and can call as many time as we want

print("--------------------------------------")
# We can also send arguments with the key = value syntax. This way the order of the arguments does not matter. but what matter? total number of argument
empInfo(empSalary = 87326472638, fullTimeEmployee = True, empName = "Alex", empId = 85276)

# Default Parameter Value. The following example shows how to use a default parameter value. If we call the function without argument, it uses the default value:
print("--------------------------------------")
def emp_info(empName, empId, empSalary = 100000, fullTimeEmployee = True):
    x = f"Employee Name: {empName.upper()} \nEmployee Id: {empId} \nEmployee Salary: {empSalary:,.4f} \nFull Time Employee: {fullTimeEmployee}"
    print(x)
# calling the function without all argument, because 2 parameter is fixed
emp_info("Sapna", 6768)

print("--------------------------------------")
# calling the function with a different argument will override the parameter
emp_info("Muktar", 3352, 134827638, False) 