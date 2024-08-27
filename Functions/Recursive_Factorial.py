def fact(n):
    # Base case: factorial of 1 (or 0) is 1
    if n <= 1:
        return 1
    # Recursive case: n * factorial of (n-1)
    else:
        return n * fact(n - 1)

# Example usage:
number = 5
print(f"The factorial of {number} is {fact(number)}")
