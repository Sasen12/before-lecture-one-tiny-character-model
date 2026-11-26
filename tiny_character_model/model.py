"""Count-based character model with optional context."""

from tiny_character_model.dataset import create_training_examples


class CharacterNgramModel:
    """Learn which character IDs follow each context by counting examples."""

    def __init__(self, context_size=1):
        if context_size < 1:
            raise ValueError("context_size must be at least 1.")

        self.context_size = context_size
        self.overall_target_counts = {}
        self.context_target_counts = {}

    def fit(self, token_ids):
        """Count overall targets and targets for each context."""
        examples = create_training_examples(token_ids, self.context_size)
        if not examples:
            raise ValueError(
                "Training text must contain more characters than context_size."
            )

        # Start fresh each time fit() is called, so repeated training does
        # not accidentally count the same text multiple times.
        self.overall_target_counts = {}
        self.context_target_counts = {}

        for context, target_id in examples:
            # Lesson 5 idea: count every target without using context.
            if target_id in self.overall_target_counts:
                self.overall_target_counts[target_id] += 1
            else:
                self.overall_target_counts[target_id] = 1

            # Lesson 6 idea: keep a separate target count for each context.
            if context not in self.context_target_counts:
                self.context_target_counts[context] = {}

            counts_for_context = self.context_target_counts[context]
            if target_id in counts_for_context:
                counts_for_context[target_id] += 1
            else:
                counts_for_context[target_id] = 1

        return self

    def most_common_overall(self):
        """Return the most frequent target ID, or None if not trained."""
        best_target_id = None
        highest_count = 0

        # If counts tie, the first target encountered remains selected.
        for target_id, count in self.overall_target_counts.items():
            if count > highest_count:
                best_target_id = target_id
                highest_count = count

        return best_target_id

    def next_token_counts(self, context):
        """Return observed next-token counts for one context."""
        context = tuple(context)
        if len(context) != self.context_size:
            raise ValueError(
                f"Expected a context of {self.context_size} token IDs, "
                f"received {len(context)}."
            )

        # Return an empty dictionary if the model never saw this context.
        return self.context_target_counts.get(context, {})
