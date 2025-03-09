# Logical operators are used to combine two or more conditional statements 
# and, or, not is used
# "or" operator returns True if one of the statements is true
# Generally we don't use logical "or" operator
def outcome(val1, val2):
    if val1%2==0 or val1>val2:
        print(val1, "is an EVEN number or", val1, "is greater than", val2)
    
outcome(5, 3)
outcome(4, 6)
