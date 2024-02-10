# Given string
input_string = "AbCdE"

# Separate lowercase and uppercase letters
lowercase_letters = ''.join(char for char in input_string if char.islower())
uppercase_letters = ''.join(char for char in input_string if char.isupper())

# Arrange the characters so that lowercase letters come first
arranged_string = lowercase_letters + uppercase_letters

# Print the arranged string
print(arranged_string)
