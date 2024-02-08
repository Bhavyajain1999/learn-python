# Given alphanumeric string input
input_string = input("Enter an alphanumeric string: ")

# Initialize an empty string to store digits
digits_only = ""

# Iterate through each character in the input string
for char in input_string:
    # Check if the character is a digit
    if char.isdigit():
        # Append the digit character to the string containing only digits
        digits_only += char

# Print the string containing only digits
print("Digits only:", digits_only)
