def find_maximum(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))


maximum = find_maximum(num1, num2, num3)


print("The maximum number is:", maximum)
