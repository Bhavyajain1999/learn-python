# Iterate through numbers from 1000 to 3000 (inclusive)
for num in range(1000, 3001):
    # Extract each digit of the number
    # Check if all digits are even
    if (num // 1000) % 2 == 0 and \
       (num // 100 % 10) % 2 == 0 and \
       (num // 10 % 10) % 2 == 0 and \
       (num % 10) % 2 == 0:
        # If all digits are even, print the number
        print(num, end=" ")

# Print a newline character to end the line
print()
