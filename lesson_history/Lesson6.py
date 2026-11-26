# Lesson 6: Using Context to Predict the Next Character
#
# In Lesson 5, we counted all target characters together.
# That meant the model made the same guess no matter what
# the input character was.
#
# Now we'll keep separate target counts for each input
# character. This gives the model a little context.
#
# This is still a small, count-based model.
# It is not a neural network, and it is not learning weights.

# Use the same training text as Lesson 5.
text = "saturday"


# Choose which input character we want to make a prediction for.
# Try changing this to "a" after you run the program once.
input_to_predict = "t"


# Show the text that supplies our training examples.
print("Training text:", text)
print()

# Print every input-and-target pair.
# Each character is paired with the character immediately after it.
print("Training examples:")

# We stop one position before the end because the last
# character has no following character to be its target.
for position in range(len(text) - 1):

    # This is the character we give to the model as context.
    input_character = text[position]

    # This is the character we want the model to predict.
    target_character = text[position + 1]

    # Display the pair so we can inspect the examples.
    print(input_character, "->", target_character)


# Make a dictionary for the overall target counts 
overall_target_counts = {}

# Make a second dictionary for context-specific counts.
#
# It will have one entry per input character.
# Each entry will contain another dictionary:
# input character -> {possible next character: count}
#
# For example, it could eventually contain:
# "t": {"u": 1}
next_character_counts = {}

# Vist each input-and-target pair in the training text 
for position in range(len(text)-1):

    # Get the input character for this example
    input_character = text[position]

     # Get the target character that follows the input.
    target_character = text[position + 1]

    
    # Update the overall target counts.
    #
    # If we have seen this target before, increase its count.
    if target_character in overall_target_counts:
        overall_target_counts[target_character] += 1

    # If this is the first time we have seen the target,
    # create it in the dictionary with a count of one.
    else:
        overall_target_counts[target_character] = 1


    # Make a place to store counts for this input character,
    # if this is the first example with that input.
    if input_character not in next_character_counts:
        next_character_counts[input_character] = {}

    
    # Now update the count for this particular input-target pair.
    #
    # If this target has followed this input before,
    # increase that pair's count.
    if target_character in next_character_counts[input_character]:
        next_character_counts[input_character][target_character] += 1

    # If this target has not followed this input before,
    # start its count at one.
    else:
        next_character_counts[input_character][target_character] = 1

# Show the overall target counts.
# For "saturday", "a" is the most common target.
print()
print("Overall target counts:")

for target_character, count in overall_target_counts.items():
    print(target_character, "appeared", count, "time(s)")

# Find the most common target overall, as in Lesson 5 
overall_guess = None
highest_overall_count = 0

# Check each target and its count.
for target_character, count in overall_target_counts.items():

    # Only replace the current guess if this count is bigger.
    # If counts tie, the first character encountered stays the guess.
    if count > highest_overall_count:
        overall_guess = target_character
        highest_overall_count = count

print()
print("Lesson 5 overal guess:", overall_guess)


# Show the context-specific counts we built.
print()
print("Next-character counts for each input:")

for input_character, target_counts in next_character_counts.items():
    print(input_character, "->", target_counts)

# Now make a prediction using the chosen input character.
print()
print("Input character:", input_to_predict)

# Check if the training text contained this input character.
if input_to_predict in next_character_counts:

    # Get the possible next characters and their counts, for this input only
    possible_targets = next_character_counts[input_to_predict]

    # Start with no best prediction and a count of 0
    context_guess = None
    highest_context_count = 0

     # Check every possible next character for this input.
    for target_character, count in possible_targets.items():

        # Replace the guess only when we find a larger count.
        # If there is a tie, the first target encountered stays.
        if count > highest_context_count:
            context_guess = target_character
            highest_context_count = count

    # Display the context-specific result.
    print("Possible next characters:", possible_targets)
    print("Context-based prediction:", context_guess)

    # The model cannot predict what follows an input it never saw.
else:
    print("The training text did not contain that input character.")




# VIEWER CHALLENGE:
# Change input_to_predict to "a".
#
# In "saturday", "a" is followed by both "t" and "d".
# Each appears once, so there is a tie.
# Because the code keeps the first target it encounters,
# it will choose "t".
#
# Try other input characters and predict the result first.










