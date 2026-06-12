
# simple substraction
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))
print("substaction of numbers :" , (a-b))
print("substaction of numbers :" , (a-c))

# using input interactive
def numbers(a, b, c, d):
    return a - b - c - d

# Take values from user
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))

# Call function with those values
result = numbers(a, b, c)
print("Result:", result)

#passing values
def numbers(a, b, c):
    return a - b - c

# Directly pass values
result = numbers(10, 3, 2)
print("Result:", result)

