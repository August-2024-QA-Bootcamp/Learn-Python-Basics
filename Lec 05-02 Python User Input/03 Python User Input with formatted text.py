empName = input("Name: ")
empId = input("Id: ")
empSalary = float(input("Salary: "))
fullTimeEmployee = input("Full Time? ")

def empInfo():
    x = f"Employee Name: {empName.upper()} \nEmployee Id: {empId} \nEmployee Salary: {empSalary:,.2f} \nFull Time Employee: {fullTimeEmployee}"
    return print(x)

print("--------------------------------------")
# We define the variables when the function is called
# User input can only accept one sets of data, not like parameterized function which can give diffeent outcome based on arguments
empInfo()