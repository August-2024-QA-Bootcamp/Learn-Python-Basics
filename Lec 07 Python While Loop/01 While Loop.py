# # Loop is a programming structure that repeats a sequence of instructions until a specific condition is met.
# Python has two primitive loop commands: while loops, for loops

"""
initialization block
while Conditional block:
    statement to print
    incremental or decremental block
"""

# Initilization block: i=1
# Conditional block: i<10
# Incremental or Decremental block: i+=1

# Incremental block: i+=1, incremented by 1, you can also write i = i+1
# Incremental block: i+=2, incremented by 2, you can also write i = i+2
# Incremental block: i+=3, incremented by 3, you can also write i = i+3

# Decremental block: i-=1, decremented by 1, you can also write i = i-1
# Decremental block: i-=2, decremented by 2, you can also write i = i-2
# Decremental block: i-=3, decremented by 3, you can also write i = i-3

# This is not mandatory to start the initialization block from 0
# This is not mandatory to increment by 1, below is an example

# Example of incremenal
i = 1
while i<5:
    print(i)
    i+=1
print("program End")
# 1, 2, 3, 4

i = 0
while i<10:
    print(i)
    i+=2
print("Porgram End")
# 0, 2, 4, 6, 8

j = 1
while j<18:
    print(j)
    j+=3
print("Porgram End")

# Example of decremenal
i = 20
while i>3:
    print(i)
    i-=3
print("Porgram End")
# 20, 17, 14, 11, 8, 5