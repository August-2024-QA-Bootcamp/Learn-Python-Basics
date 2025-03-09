# We can use input() to provide value from terminal as we wish
a = input("Please provide the value of a: ")
b = input("Please provide the value of b: ")

if a>b:
    print(a, "is grether than", b)
elif a<b:
    print(a, "is smaller than", b)
elif a==b:
    print(a, "is equal to", b)
else:
    print("The System failed to execute this order")