# Given string
input_string = input("Enter a string: ")

# Calculate the length of the string
length = len(input_string)

# Check if the length of the string is even or odd
if length % 2 == 0:
    # If the length is even, compare the first half with the reversed second half
    first_half = input_string[:length // 2]
    second_half = input_string[length // 2:]
else:
    # If the length is odd, compare the first half with the reversed second half (excluding the middle character)
    first_half = input_string[:length // 2]
    second_half = input_string[length // 2 + 1:]

# Check if the first half is equal to the reversed second half
if first_half == second_half:
    print("The string is symmetrical.")
else:
    print("The string is not symmetrical.")
