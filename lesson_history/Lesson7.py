# Lesson 7: Our First Tiny Text Generator
#
# The first version used only one character as context.
# That gave the model many unrelated choices.
#
# This version looks at the previous TWO characters
# when choosing the next one.
#
# The model learns character patterns by counting them.
# It is a tiny statistical model, not a neural network
# or a conversational chatbot.


import random


# These short phrases are the text the model learns from.
# Spaces are included, so the model can learn where words
# begin and end.
training_text = (
    "hello friend "
    "hello there "
    "hi there "
    "how are you "
    "good to see you "
)


# The model will use this many previous characters
# as context when it chooses the next character.
context_size = 2


# Generation must start with two characters because
# context_size is 2. Try changing this to another
# two-character beginning found in the training text.
starting_text = "he"


# Choose how many characters to try to generate
# after the starting text.
characters_to_generate = 50


# Show the text the model will learn from.
print("Training text:")
print(training_text)
print()


# Show the context length and starting text.
print("Context size:", context_size, "characters")
print("Starting text:", starting_text)


# This dictionary will store the patterns found in the text.
#
# Each key will be a two-character context.
# Its value will be another dictionary containing:
#     possible next character: how often it followed
#
# For example, it might contain:
#     "he": {"l": 2}
#
# This means that in the training text, the context "he"
# was followed by "l" two times.
context_counts = {}


# Move through the training text and collect examples.
#
# We stop early enough that each example has:
# 1. A full context of two characters.
# 2. A character after that context to use as the target.
for position in range(len(training_text) - context_size):

    # Take two characters from the current position.
    # These are the characters the model will use as context.
    context = training_text[position:position + context_size]

    # The character immediately after the context
    # is the target we want the model to predict.
    target_character = training_text[position + context_size]


    # If this context has not appeared before,
    # create an empty dictionary to store its target counts.
    if context not in context_counts:
        context_counts[context] = {}


    # If this target has followed the context before,
    # increase its count.
    if target_character in context_counts[context]:
        context_counts[context][target_character] += 1

    # Otherwise, this is the first time we've seen
    # this context followed by this target.
    else:
        context_counts[context][target_character] = 1


# Print the patterns counted from the training text.
print()
print("Learned context patterns:")

for context, target_counts in context_counts.items():
    print(repr(context), "->", target_counts)


# Begin the generated text with the starting text.
generated_text = starting_text


# Each new prediction will use the most recent
# context_size characters in the generated text.
for step in range(characters_to_generate):

    # Get the most recent two characters.
    # Those are the context for the next prediction.
    context = generated_text[-context_size:]


    # If the model never saw this context in the training text,
    # it has no examples to use for its next prediction.
    if context not in context_counts:
        print()
        print("The model has no learned continuation for:",
              repr(context))
        break


    # Get the possible next characters and how often
    # each one followed this context.
    possible_targets = context_counts[context]


    # Make a list of possible next characters.
    #
    # If a target appeared more often, add it to the list
    # more times. That makes it more likely to be selected.
    weighted_choices = []

    for target_character, count in possible_targets.items():

        # Add this target once for every time it appeared.
        for repeat in range(count):
            weighted_choices.append(target_character)


    # Randomly choose one of the possible next characters.
    # More frequent targets have a higher chance of being chosen.
    next_character = random.choice(weighted_choices)


    # Add the chosen character to the generated text.
    generated_text += next_character


# Show the text that was generated.
print()
print("Generated text:")
print(generated_text)


# VIEWER CHALLENGE:
# Try changing the starting text or adding phrases
# to the training text.
#
# Predict how the generated output might change, then run it.
#
# The output can vary between runs because the model
# chooses randomly from the learned possibilities.