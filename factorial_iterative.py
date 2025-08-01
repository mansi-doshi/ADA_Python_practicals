def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

num = int(input("enter number:"))
print("Factorial (Iterative):", factorial_iterative(num))
