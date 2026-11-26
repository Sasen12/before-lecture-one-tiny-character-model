"""Create input-context and next-character target examples."""


def create_training_examples(token_ids, context_size=1):
    """Return examples as (context, target_id) pairs.

    A context is a tuple of one or more token IDs. The target is the
    token immediately after that context in the original text.
    """
    if context_size < 1:
        raise ValueError("context_size must be at least 1.")

    examples = []

    # Stop when the current context would have no target after it.
    for position in range(len(token_ids) - context_size):
        context = tuple(token_ids[position:position + context_size])
        target_id = token_ids[position + context_size]
        examples.append((context, target_id))

    return examples
