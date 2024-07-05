def gcd_range(a, b):
    # If a is equal to b, the GCD is a
    if a == b:
        return a
    # Otherwise, the GCD of the range from a to b is 1
    return 1

# Read input
input_line = input().strip()
a, b = map(int, input_line.split())

# Calculate GCD of the range
result = gcd_range(a, b)
print(result)