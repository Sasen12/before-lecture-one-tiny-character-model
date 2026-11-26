# Lesson 5: A Simple Next-Character Predictor
#
# Last lesson, we used Python to make input-and-target
# pairs from text.
#
# Today, we'll count the target characters and predict
# whichever target appeared most often.
#
# This is a very simple frequency-based model.
# It does not use the input character as context yet.

# Use the same text as lesson 4 so we can build from it
text="saturday"

# Show the text we are learning from.
print("Training text:",text)
print()

# First, show the input-target examples again
print("Training examples:")

for position in range(len(text) - 1):
    # Get the character at the current postion 
    input_character = text[position]
    # Get the character that comes after it
    target_character = text[position + 1]
    # Display the input and target characters for this example
    print(input_character, "->", target_character)


# Make an empty dictionary to count the targets
#
# The character will the dictionary key
# Its count will be the value
target_counts = {}


# Move through the text and count each target character.
for position in range(len(text)-1):
    # Find the target character for this position.
    target_character = text[position + 1]

    # If we've counted this before, add one to its exisiting count
    if target_character in target_counts:
        target_counts[target_character] += 1

    # If this is the first time, start the count from one

    else:
        target_counts[target_character] = 1

# Print the counts so we can inspect what the program has learned from the examples
print()
print("Target character counts:")

for character, count in target_counts.items():
    print(character, "appeared", count, "time(s)")

# Now find the target character with its highest count
# We start with no best character and a count of zero
most_common_character= None
highest_count = 0

# Check each character and its count
for character, count in target_counts.items():
    # If this count is higher than the best count so far,
    # rememmber this character as the next best guess
    if count > highest_count:
        most_common_character = character
        highest_count = count

# Show the simple models prediction.
print()
print("Most common targets:", most_common_character)
print ("Model's guess for the next character", most_common_character)


# VIEWER CHALLENGE:
# Change the training text and predict how the target
# counts and the model's guess will change.

