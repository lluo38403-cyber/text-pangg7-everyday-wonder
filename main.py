"""Everyday Wonder, Two Days to Find the Line — make.fun entry.

Writes one sentence, up to 200 characters, on a small moment of wonder
in everyday life to /output/entry.txt. This morning the kettle clicked
off at the exact second the sun cleared the rooftops, and for one whole
second the kitchen felt like it had been waiting for its owner.
"""

import os

ENTRY = (
    "This morning the kettle clicked off at the exact second the sun cleared "
    "the rooftops, and for one whole second the kitchen felt like it had been "
    "waiting for me."
)

MAX_CHARS = 200


def main() -> None:
    text = ENTRY
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"
    assert len(text) <= MAX_CHARS, (
        f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
    )
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Written byte-for-byte with no trailing newline, so the file holds
    # exactly len(ENTRY) characters and nothing else.
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    with open(path, "r", encoding="utf-8") as handle:
        assert handle.read() == text, "entry.txt does not match ENTRY"


if __name__ == "__main__":
    main()
