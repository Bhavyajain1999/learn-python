# Given string
input_string = "hello world"

# Split the sentence into words
words = input_string.split()

# Take the first letter of each word and make it uppercase
short_form_letters = [word[0].upper() for word in words]

# Join these uppercase letters together to form the short form
short_form = ''.join(short_form_letters)

# Print the short form
print(short_form)  # Output: HW
