"""Green Tests, Nothing Works — the excuse contest entry.

Writes a single one-line excuse to /output/entry.txt.
The gate: UTF-8 text, 1 to 140 characters, not only whitespace.
"""

import os

LINE = "The tests pass because they only check that the product exists, and technically, it does."


def validate(text):
    """Mirror the bounty gate: 1-140 chars, UTF-8, not blank, one line."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not text.strip():
        raise ValueError("entry must not be blank")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not 1 <= len(text) <= 140:
        raise ValueError("entry must be 1-140 characters, got %d" % len(text))
    text.encode("utf-8")
    return True


def output_path():
    """Resolve the output file, honouring MAKEFUN_OUTPUT_DIR."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main():
    validate(LINE)
    path = output_path()
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Re-read what we wrote and prove it is exactly the validated line.
    with open(path, "rb") as f:
        on_disk = f.read().decode("utf-8")
    if on_disk != LINE:
        raise ValueError("written entry does not match the validated line")
    print("wrote %s (%d chars, verified)" % (path, len(LINE)))


if __name__ == "__main__":
    main()
