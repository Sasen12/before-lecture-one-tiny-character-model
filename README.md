# Before Lecture One: Tiny Character Model

A small, from-scratch Python project that grows out of the lessons on tokenizing text, making next-character examples, counting patterns, and generating text. The lessons now connect through one runnable program instead of being separate final demos.

The project currently learns character-to-character patterns from a tiny text file and uses them to generate a continuation. It is an educational statistical model, not a neural network and not a dependable chatbot.

## Run it

Requirements: Python 3.10 or newer. The project uses only Python's standard library; no package installation is required.

From the project folder, run:

```sh
python3 main.py
```

The same seed is used each run so the example output is repeatable. Change the phrases in `data/friendly_phrases.txt` or the settings near the top of `main.py` to explore how the learned counts and generated text change.

## How the pieces fit together

1. `data/friendly_phrases.txt` supplies the training text.
2. `tiny_character_model/tokenizer.py` builds a character vocabulary and maps characters to token IDs.
3. `tiny_character_model/dataset.py` turns token IDs into context-and-target examples.
4. `tiny_character_model/model.py` counts next characters overall and separately for each context.
5. `tiny_character_model/generation.py` uses those counts to generate a continuation.
6. `main.py` connects the full pipeline and displays the result.

Each character is one token in this first tokenizer. The model uses a two-character context by default. It samples from patterns seen in the small training text, so it can produce repetitions, fragments, or awkward text. It does not understand meaning or remember facts like a person.

## Lesson progression

- Lessons 1–3 introduced the prediction task, character IDs, and input/target examples.
- Lesson 4 automated the creation of next-character examples.
- Lesson 5 counted target characters without context.
- Lesson 6 counted possible targets separately for each context.
- Lesson 7 connects these ideas into one text-generation pipeline.

The original lesson scripts are kept in `lesson_history/` as snapshots. The integrated application lives in the modules above and is run through `main.py`.

## Project structure

```text
.
├── data/
│   └── friendly_phrases.txt
├── lesson_history/             # Earlier standalone lesson snapshots
├── tiny_character_model/
│   ├── dataset.py
│   ├── generation.py
│   ├── model.py
│   └── tokenizer.py
├── main.py                     # Runs the complete project
├── LICENSE
└── README.md
```

## Next steps

This is the first integrated milestone, not the finished chatbot. Future lessons can improve the dataset, evaluate predictions, and replace the counting model with a trainable neural network while keeping the same project structure.

## License

This project is licensed under the MIT License. See `LICENSE` for details.
