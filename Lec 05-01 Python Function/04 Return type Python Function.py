print("--------------------------------------")
# Return Values: To let a function return a value, use the return statement
def yearlySalary(monthlySalary):
    return 12*monthlySalary

print(yearlySalary(5000))

print("--------------------------------------")
def yearlyBenefit(monthlyBenefit):
    x = 12*monthlyBenefit
    return print(x)
    print("Work") # This line is not executing because return is the last statement of a return type function

yearlyBenefit(300)

