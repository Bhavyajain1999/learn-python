# Given sentence
sentence = input("Enter a sentence: ")
word_to_find = input("Enter the word to find: ")

# Split the sentence into words
words = sentence.split()

# Initialize a variable to store the position of the word
position = None

# Iterate through the words and find the position of the word
for idx in range(len(words)):
    if words[idx] == word_to_find:
        position = idx + 1  # Adding 1 to make it human-readable (not zero-based)
        break

# Print the position of the word
if position is not None:
    print(f"The word '{word_to_find}' is located at position {position}.")
else:
    print(f"The word '{word_to_find}' is not found in the sentence.")
