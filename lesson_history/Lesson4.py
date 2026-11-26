# Lesson 4: Automatically Creating Training Examples
#
# In Lesson 3, we selected character positions ourselves.
# This time, a loop will move through the text and make
# each input-and-target pair for us.
#
# We are still only preparing examples.
# Nothing is learning or changing yet.


# Start with a longer peice of text so the loop has more to work with.


text = "hello"


# Print the text so we can see what the program is working with.
print("Full text:",text)
print()
print("Training examples:")

# Each example uses one character as the imput
# and the character that comes after it as the target.
#
# We stop one postion before the end of the text, because there is no character after the last one.
for position in range(len(text) - 1):
    # Get the character at the current postion 
    input_character = text[position]
    # Get the character that comes after it
    target_character = text[position + 1]
    # Display the input and target characters for this example
    print("Input character:", input_character)
    print("Target character:", target_character)

# The number of pairs shoudl be one less than the number of characters in the text.
number_of_examples = len(text) -1

print()
print("Number of characterd in the text:", len(text))
print("Number of training examples we can make:", number_of_examples)

# VIEWER CHALLLENGE 
# Change the text to different word
#
# Before running the program predict the number of pairs 
# and how many exmaples it will create
#
# Then run it and compare the result with your prediction.the



