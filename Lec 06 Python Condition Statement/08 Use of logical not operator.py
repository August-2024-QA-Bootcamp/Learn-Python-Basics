# Logical operators are used to combine two or more conditional statements 
# and, or, not is used
# logical "not" operator, Reverse the result, returns False if the result is true

def outcome(val1, val2):
    if val1%2==0 and val1>val2:
        print(val1, "is an EVEN number and", val1, "is greater than", val2)
    elif not(val1%2==0 and val1>val2):
        print(val1, "is a not EVEN number [ODD number] and", val1, "is not greater [smaller] than", val2)

outcome(12, 3)
outcome(11, 13)

