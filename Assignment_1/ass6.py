def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result



num = int(input("Enter a non-negative integer: "))

print("Factorial of", num, "is:", factorial(num))
