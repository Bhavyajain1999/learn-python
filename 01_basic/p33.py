# Given string
input_string = input("Enter a string: ")

# Split the string into words
words = input_string.split()

# Reverse the order of words
reversed_words = words[::-1]

# Join the reversed words back into a string
reversed_string = ' '.join(reversed_words)

# Print the reversed string
print("Reversed string:", reversed_string)
