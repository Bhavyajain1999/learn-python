# Iterate through numbers from 2000 to 3200 (inclusive)
for num in range(2000, 3201):
    # Check if the number is divisible by 7 and not a multiple of 5
    if num % 7 == 0 and num % 5 != 0:
        # Print the number followed by a comma and a space
        print(num, end=", ")

# Print a newline character to end the line
print()
