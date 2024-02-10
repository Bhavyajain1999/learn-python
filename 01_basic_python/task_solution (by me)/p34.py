# Input sentences
sentence1 = input("Enter the first sentence: ")
sentence2 = input("Enter the second sentence: ")

# Split sentences into words
words1 = sentence1.split()
words2 = sentence2.split()

# Initialize a list to store uncommon words
uncommon_words = []

# Check words in the first sentence
for word in words1:
    if word not in words2 and words1.count(word) == 1:
        uncommon_words.append(word)

# Check words in the second sentence
for word in words2:
    if word not in words1 and words2.count(word) == 1:
        uncommon_words.append(word)

# Print the list of uncommon words
if uncommon_words:
    print("Uncommon words:", uncommon_words)
else:
    print("No uncommon words found.")
