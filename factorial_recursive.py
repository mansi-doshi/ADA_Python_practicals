def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)


num = int(input("enter number:"))
print("Factorial (Recursive):", factorial_recursive(num))
