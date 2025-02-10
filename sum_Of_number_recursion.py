def sum_recursive(n):
    if n <= 0:  # Base case
        return 0
    s=n + sum_recursive(n - 1)
    return s  # Recursive call

n = int(input("Enter a number: "))
print("Sum:", sum_recursive(n))  # Call function and print result
