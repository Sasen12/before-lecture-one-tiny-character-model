# Lesson 1: Predicting what comes next
#
# This program demonstrates the basic task we're working toward:
# look at part of a sequence and predict what comes after it.
#
# It does NOT train or learn yet. We choose the prediction ourselves.

#Start with a short short
text = "cat"

# Python counts psotions from 0, so the first letter is at position 0, the second at position 1, and so on.
current_character = text[0]

#Get the next character immediately after the current one.
next_character = text [1]

# Show the word and the characters we selected.
print("The word is:", text)
print("Curent character:", current_character)
print("Next character:", next_character)

# Make a pretend prediction 
# This is Hard-coded: the program did not learn to choose "a"
prediction ="a"

#Compare the prediction to the actual next character.
#The result will be True if they mathch, and False if they don't.
was_correct= prediction == next_character 

# Show the prediction and whether it matched
print("Model's guess:", prediction)
print("correct next character:", next_character)
print("Was the prediction correct?", was_correct)

#Try changing text to "cup" and see what happens. The program will still predict "a" even though the next character is "u".




