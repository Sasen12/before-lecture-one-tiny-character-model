"""Generate text by sampling the model's counted continuations."""

import random


def generate_text(
    tokenizer,
    model,
    prompt,
    max_new_characters=50,
    seed=None,
):
    """Extend prompt one character at a time using learned counts.

    More frequent continuations are placed in the random-choice list
    more times, so they have a higher chance of being selected.
    """
    if max_new_characters < 0:
        raise ValueError("max_new_characters cannot be negative.")

    generated_ids = tokenizer.encode(prompt)
    if len(generated_ids) < model.context_size:
        raise ValueError(
            "The prompt must contain at least "
            f"{model.context_size} characters for this model."
        )

    # A local random generator makes results reproducible when a seed is given.
    random_generator = random.Random(seed)

    for _ in range(max_new_characters):
        # Use the most recent characters as the next prediction context.
        context = tuple(generated_ids[-model.context_size:])
        possible_targets = model.next_token_counts(context)

        # Stop cleanly if the model has no training example for this context.
        if not possible_targets:
            break

        weighted_choices = []
        for target_id, count in possible_targets.items():
            # Repeating an ID makes it more likely in random.choice().
            for _ in range(count):
                weighted_choices.append(target_id)

        next_id = random_generator.choice(weighted_choices)
        generated_ids.append(next_id)

    return tokenizer.decode(generated_ids)
