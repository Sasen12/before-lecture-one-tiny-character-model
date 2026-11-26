"""Run the complete tiny character-model project."""

from pathlib import Path

from tiny_character_model.dataset import create_training_examples
from tiny_character_model.generation import generate_text
from tiny_character_model.model import CharacterNgramModel
from tiny_character_model.tokenizer import CharacterTokenizer


PROJECT_ROOT = Path(__file__).parent
TRAINING_FILE = PROJECT_ROOT / "data" / "friendly_phrases.txt"
CONTEXT_SIZE = 2
STARTING_PROMPT = "he"
NEW_CHARACTERS = 50
RANDOM_SEED = 7


def main():
    # Read the examples the model will learn from.
    training_text = TRAINING_FILE.read_text(encoding="utf-8")

    # Build a character tokenizer from the training text.
    # In this project, each character is one token.
    tokenizer = CharacterTokenizer().fit(training_text)
    token_ids = tokenizer.encode(training_text)

    # Make context-and-target examples from the token IDs.
    # The same function works with one-character or longer contexts.
    examples = create_training_examples(token_ids, CONTEXT_SIZE)

    # Train the count-based model on those examples.
    model = CharacterNgramModel(context_size=CONTEXT_SIZE)
    model.fit(token_ids)

    # Show how the project's pieces connect.
    print("BEFORE LECTURE ONE: TINY CHARACTER MODEL")
    print("=" * 42)
    print("Training text:")
    print(training_text)
    print("Vocabulary size:", len(tokenizer.vocabulary))
    print("Training examples:", len(examples))
    print("Context size:", CONTEXT_SIZE, "characters")

    # Display the Lesson 5 style guess based on all targets.
    overall_guess = model.most_common_overall()
    if overall_guess is not None:
        print(
            "Most common next character overall:",
            repr(tokenizer.decode([overall_guess])),
        )

    # Show what the model learned for the prompt's final context.
    prompt_ids = tokenizer.encode(STARTING_PROMPT)
    prompt_context = tuple(prompt_ids[-CONTEXT_SIZE:])
    next_token_counts = model.next_token_counts(prompt_context)
    readable_counts = {
        tokenizer.decode([token_id]): count
        for token_id, count in next_token_counts.items()
    }
    print("Starting prompt:", repr(STARTING_PROMPT))
    print("Possible next characters from prompt:", readable_counts)

    # Generate text by repeatedly predicting one character,
    # adding it to the prompt, and using the latest context again.
    generated = generate_text(
        tokenizer=tokenizer,
        model=model,
        prompt=STARTING_PROMPT,
        max_new_characters=NEW_CHARACTERS,
        seed=RANDOM_SEED,
    )

    print("Generated text:")
    print(generated)
    print()
    print(
        "This tiny statistical model recombines character patterns. "
        "It does not understand the text or act as a reliable chatbot."
    )


if __name__ == "__main__":
    main()
