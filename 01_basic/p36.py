# Get input from the user
input_string = input("Enter a string: ")

# Initialize an empty string to store unique characters
unique_string = ""

# Iterate through each character in the input string
for char in input_string:
    # Check if the character is not already in the unique string
    if char not in unique_string:
        # If not, add it to the unique string
        unique_string += char

# Print the string with duplicate characters removed
print("String with duplicates removed:", unique_string)
