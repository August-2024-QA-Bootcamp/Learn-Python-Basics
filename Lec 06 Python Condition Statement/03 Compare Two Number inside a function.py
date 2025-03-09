# compareTwoNumber is an user define function
# a and b is called parameter
def compareTwoNumber(a, b):
    if a>b:
        print(a, "is grether than", b)
    elif a<b:
        print(a, "is smaller than", b)
    elif a==b:
        print(a, "is equal to", b)
    else:
        print("The System failed to execute this order")

# what is the advantage of creating parametrized function?
# we can reuse the function by different arguments
# Here 2 value is called argument
compareTwoNumber(2231, 8650)
compareTwoNumber(91, 50)
compareTwoNumber(31, 31)