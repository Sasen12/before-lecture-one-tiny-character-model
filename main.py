# Lesson 7: Connecting the Pieces
#
# The earlier lessons introduced each idea separately:
# text, character IDs, input-and-target examples, and next-character counts.
# This program connects those ideas into one small text generator.
#
# This is a count-based character model. It is useful for learning how
# training data and context work, but it is not a neural network and does
# not understand what it generates.

from pathlib import Path

from tiny_character_model.dataset import create_training_examples
from tiny_character_model.generation import generate_text
from tiny_character_model.model import CharacterNgramModel
from tiny_character_model.tokenizer import CharacterTokenizer


# __file__ is the path to this script. Building paths from it means the
# data file can be found even if Python is launched from another folder.
PROJECT_FOLDER = Path(__file__).parent
TRAINING_FILE = PROJECT_FOLDER / "data" / "friendly_phrases.txt"

# These are the settings viewers can experiment with.
CONTEXT_SIZE = 2
STARTING_TEXT = "he"
NEW_CHARACTERS = 50
RANDOM_SEED = 7


def main():
    """Run the training and text-generation pipeline."""

    # Step 1: Read the examples the model will learn from.
    training_text = TRAINING_FILE.read_text(encoding="utf-8").strip()

    if not training_text:
        raise ValueError("The training text file is empty.")

    print("Lesson 7: Connecting the Pieces")
    print()
    print("Training text:")
    print(training_text)
    print()

    # Step 2: Give each unique character in the training text a number.
    tokenizer = CharacterTokenizer()
    tokenizer.fit(training_text)
    token_ids = tokenizer.encode(training_text)

    print("Characters in training text:", len(training_text))
    print("Unique character IDs:", len(tokenizer.vocabulary))
    print()

    # Step 3: Make context-and-target examples from the IDs.
    # For a context size of 2, an example might be: "he" -> "l".
    examples = create_training_examples(token_ids, context_size=CONTEXT_SIZE)

    print("Context size:", CONTEXT_SIZE)
    print("Training examples created:", len(examples))
    print()
    print("A few training examples:")

    for context_ids, target_id in examples[:10]:
        context_text = tokenizer.decode(context_ids)
        target_text = tokenizer.decode([target_id])
        print(f"{context_text!r} -> {target_text!r}")

    # Step 4: Train the count-based model.
    # Here, "train" means count which IDs follow each context.
    # CharacterNgramModel.fit() receives the token IDs and creates its
    # own examples internally, so we pass it the original encoded text.
    model = CharacterNgramModel(context_size=CONTEXT_SIZE)
    model.fit(token_ids)

    # Step 5: Check that the prompt is the right length and uses known chars.
    if len(STARTING_TEXT) != CONTEXT_SIZE:
        raise ValueError(
            "The starting text must contain exactly "
            f"{CONTEXT_SIZE} characters to match CONTEXT_SIZE."
        )

    # Step 6: Generate from the patterns the model counted.
    # The fixed seed makes the same choices each time the program runs.
    generated_text = generate_text(
        tokenizer=tokenizer,
        model=model,
        prompt=STARTING_TEXT,
        max_new_characters=NEW_CHARACTERS,
        seed=RANDOM_SEED,
    )

    print()
    print("Starting text:", STARTING_TEXT)
    print("Generated text:")
    print(generated_text)

    # VIEWER CHALLENGE
    # Change STARTING_TEXT to a different two-character prompt.
    # Before running the program, predict how the generated text might change.
    # Then run it and compare your prediction with the result.
    #
    # You can also change the training phrases in:
    # data/friendly_phrases.txt
    # Predict how changing the training text might affect what the model generates.


if __name__ == "__main__":
    main()
