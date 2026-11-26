"""Turn text into character IDs and IDs back into text."""


class CharacterTokenizer:
    """A simple tokenizer that treats each character as one token."""

    def __init__(self):
        # The vocabulary is the list of distinct characters seen in training.
        self.vocabulary = []

        # These dictionaries let us move between characters and numeric IDs.
        self.character_to_id = {}
        self.id_to_character = {}

    def fit(self, text):
        """Build a consistent character-to-ID mapping from text."""
        if not text:
            raise ValueError("Cannot build a tokenizer from empty text.")

        # Sorting makes the IDs predictable for the same training text.
        self.vocabulary = sorted(set(text))

        # Give every vocabulary character an integer ID starting at zero.
        self.character_to_id = {
            character: token_id
            for token_id, character in enumerate(self.vocabulary)
        }

        # Build the reverse mapping so generated IDs can be decoded later.
        self.id_to_character = {
            token_id: character
            for character, token_id in self.character_to_id.items()
        }
        return self

    def encode(self, text):
        """Convert every character in text into its token ID."""
        if not self.character_to_id:
            raise RuntimeError("Call fit() before encoding text.")

        # Explain an unknown character clearly instead of exposing a KeyError.
        unknown_characters = sorted(set(text) - set(self.character_to_id))
        if unknown_characters:
            raise ValueError(
                "Text contains characters missing from the training "
                f"vocabulary: {unknown_characters!r}"
            )

        return [self.character_to_id[character] for character in text]

    def decode(self, token_ids):
        """Convert a sequence of token IDs back into readable text."""
        if not self.id_to_character:
            raise RuntimeError("Call fit() before decoding token IDs.")

        try:
            return "".join(self.id_to_character[token_id] for token_id in token_ids)
        except KeyError as error:
            raise ValueError(f"Unknown token ID: {error.args[0]}") from error
