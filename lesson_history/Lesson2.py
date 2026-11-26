# LESSON 2: Turning characters into numbers
#
# Computers represent information using numbers.
# A tokenizer converts text into smaller pieces and represents
# those pieces with numbers.
#
# For this first tokenizer, each individual character is one token.
# This is only a demonstration: it is not a trained AI model.

# Store the word we want to worth with
# Later, try changing this word to see how the ouput changes.
text = "cat"

# A string is a sequence of character.
# list(text) turns sequence into a list with one character per item.
characters = list(text)

# Print both versions to see the difference
print("Text:", text)
print("Characters:", characters)


# vocabulary is the colleection of diffrent characters.
# this tokenizer knows about
#
# set(text) collects each character only once
# sorted(...) puts them in alphabetical order
vocabulary = sorted(set(text))

print("vocabulary:", vocabulary)

# Create an empty dictionary to connect each character to a number
# These numbers are called "indices" or "IDs"
char_to_id={}

# enumerate(...) goes through each character in the vocabulary and gives it a number, 
# starting with 0 for the first character, 1 for the second, and so on.

# On each loop:
#  number is the ID we are asigning
# character is the character reciving that id 

for number, character in enumerate(vocabulary):
    char_to_id[character] = number

# Show the character-to-Id mapping we created 
print("Character to ID mapping:", char_to_id)

# Encoding means turning characters into number IDs.
#
# Start with an empty list. We will add one ID for each character in the orignal word.
encoded= []

# Go through the word one character at a time.
for character in text:
    # Look up the character's ID in our dictionary.
    # then add that ID to the list of encoded IDs.
    encoded.append(char_to_id[character])


# Show the word represented as a list of numbers.
print("Encoded:",encoded)

# to decode the numbers, we need a dictonary that goes the other way: from IDs to characters.
id_to_char = {}

# Look at every character and ID in the first dictionary we made, and add the reverse mapping to the new dictionary.
for character, number in char_to_id.items():
    #store the character in the new dictionary, using the ID as the key.
    id_to_char[number] = character


print("ID to Character:", id_to_char)


# Decoding mean converting  the IDs back into characters.
#
# Start with an empty string. We will rebuild the original word one character at a time.
decoded = ""

# Go through the encoded IDs in the orignal order 
for number in encoded:
    # Find the character for this ID and add it to the decoded word
    decoded += id_to_char[number]


print("Decoded:", decoded)


# VIEWER CHALLENGE:
# Change the text= "cat" to a different word such as cab
# Run the program and compare the vocabulary, encoded, and decoded outputs to see how they change.
#
# What changed? Why does the program still works?








