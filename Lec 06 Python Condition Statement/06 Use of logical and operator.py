# Logical operators are used to combine two or more conditional statements 
# and, or, not is used
# "and" operator Returns True if both statements are true
def outcome(val1, val2):
    if val1%2==0 and val1>val2:
        print(val1, "is an EVEN number and", val1, "is greater than", val2)
    elif val1%2==0 and val1<val2:
        print(val1, "is an EVEN number and", val1, "is smaller than", val2)
    elif val1%2==0 and val1>=val2:
        print(val1, "is an EVEN number and", val1, "is greater than or equal to", val2)
    elif val1%2==0 and val1<=val2:
        print(val1, "is an EVEN number and", val1, "is smaller than or equal to", val2)
    elif val1%2==1 and val1>val2:
        print(val1, "is an ODD number and", val1, "is greater than", val2)
    elif val1%2==1 and val1<val2:
        print(val1, "is an ODD number and", val1, "is smaller than", val2)
    elif val1%2==1 and val1>=val2:
        print(val1, "is an ODD number and", val1, "is greater than or equal to", val2)
    elif val1%2==1 and val1<=val2:
        print(val1, "is an ODD number and", val1, "is smaller than or equal to", val2)
    else:
        print("Please provide a valid number for val1 and val2")

outcome(345273, 648362)
outcome(42, 42)
outcome(7, 7)