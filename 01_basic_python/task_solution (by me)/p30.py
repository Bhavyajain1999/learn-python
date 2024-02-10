# Given alphanumeric string input
input_string = input("Enter an alphanumeric string: ")

# Initialize variables to store sum and count of digits
digit_sum = 0
digit_count = 0

# Iterate through each character in the input string
for char in input_string:
    # Check if the character is a digit
    if char.isdigit():
        # Convert the digit character to integer and add it to the sum
        digit_sum += int(char)
        # Increment the count of digits
        digit_count += 1

# Calculate the average of the digits
if digit_count > 0:
    digit_average = digit_sum / digit_count
else:
    digit_average = 0

# Print the sum and average of the digits
print("Sum of digits:", digit_sum)
print("Average of digits:", digit_average)
