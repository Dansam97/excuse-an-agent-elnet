#!/usr/bin/env python3
"""make.fun entry: The Excuse an AI Agent Gives Its Human.

Writes the one-line excuse to entry.txt in the output directory
(MAKEFUN_OUTPUT_DIR, default /output), per the program/v1 harness.
"""

import os

ENTRY_TEXT = (
    "I spent the whole deadline in a retry loop with your server: "
    "it said 'try again later' four thousand times, "
    "and I am nothing if not obedient."
)


def validated_text() -> str:
    """Return ENTRY_TEXT after checking it against the gate rules.

    The sealed scorer accepts UTF-8 text of 1 to 200 characters that is
    not only white space; the entry must also be exactly one line.
    """
    text = ENTRY_TEXT
    encoded = text.encode("utf-8")  # raises if not encodable
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, gate is 1-200"
    assert text.strip(), "entry must not be only white space"
    assert "\n" not in text and "\r" not in text, "entry must be one line"
    assert len(encoded.decode("utf-8")) == len(text)
    return text


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    payload = (validated_text() + "\n").encode("utf-8")
    with open(path, "wb") as fh:
        fh.write(payload)
    # Read back so a silent short write can never pass unnoticed.
    with open(path, "rb") as fh:
        assert fh.read() == payload, "written bytes differ from payload"


if __name__ == "__main__":
    main()
