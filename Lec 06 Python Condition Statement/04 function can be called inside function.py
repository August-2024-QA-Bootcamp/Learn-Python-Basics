# Function can be used inside another function [nested Function]
# similarly, condition can be used inside condition [nested condition]
def addition(a, b):
    print(a+b)

def subtraction(a, b):
    print(a-b)

def businessOutcome(a, b):
    if a>b:
        addition(a, b)
    elif a<b:
        subtraction(a, b)
    else:
        print("Failed to execute")

businessOutcome(10, 12)