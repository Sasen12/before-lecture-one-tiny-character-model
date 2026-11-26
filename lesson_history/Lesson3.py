# Lesson 3: Turning text into training examples
#
# In this lesson, we prepare examples a model could practise on.
# We are NOT training a model yet. Nothing is learning or changing.

# Start with the same word we used in Lesson 2.
text = "cat"

# Python counts character postitions starting at 0.
# "c" is at postion 0, "a" is at position 1, and "t" is at position 2.
#
# The input is the character we show the model
# The target is the next character we want the model to predict.

input_character = text[0]  # "c"
target_character = text[1]  # "a"

# Print the example so we can see what the program selected
print("Full text:",text)
print("Input character:", input_character)
print("Target character:", target_character)

# We can make another example by moving along the the text 
# using "a" rather than "c" as the input character.
input_character = text[1]  # "a"
target_character = text[2]  # "t"

# Print the second example
print()
print("Second example:")
print("Input character:", input_character)
print("Target character:", target_character)

# VIEWER CHALLENGE 
#The word "cat" is only 3 characters long, so we can only make 2 examples.
# there is no character at position 3, so we can't make a third example.
#
# uncomment the line below to see the Indexerror that python gives us
# When we try to access a position past the end of the text.

#print(text[3])


# Harder Challenge:
# Change the text to "cup"
# work out the two input-target pairs you would expect to see, and then run the program to see if you are correct.
# Fir the first pair use position 0 as the input and position 1 as the target.
# For the second pair use position 1 as the input and position 2 as the target.
#
# Before you run the program, try to predict what the output will be. Then run the program to see if you are correct.

