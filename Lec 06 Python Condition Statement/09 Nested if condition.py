
def outcome(val1, val2):
    if val1%2==0:
        if val1>val2:
            print(val1, "is an EVEN number and", val1, "is greater than", val2)
        elif val1<val2:
            print(val1, "is an EVEN number and", val1, "is smaller than", val2)
        elif val1<=val2:
            print(val1, "is an EVEN number and", val1, "is smaller than or equal to", val2)
        elif val1>=val2:
            print(val1, "is an EVEN number and", val1, "is greter than or equal to", val2)
    elif val1%2==1:
        if val1>val2:
            print(val1, "is an ODD number and", val1, "is greater than", val2)
        elif val1<val2:
            print(val1, "is an ODD number and", val1, "is smaller than", val2)
        elif val1<=val2:
            print(val1, "is an ODD number and", val1, "is smaller than or equal to", val2)
        elif val1>=val2:
            print(val1, "is an ODD number and", val1, "is greter than or equal to", val2)
    else:
        print("Please provide valid numbers")

outcome(2, 4)
outcome(3, 4)
outcome(3, 3)