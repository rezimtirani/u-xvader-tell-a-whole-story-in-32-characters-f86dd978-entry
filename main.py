"""Tell a Whole Story in 32 Characters.

Writes one Wi-Fi network name to $MAKEFUN_OUTPUT_DIR/entry.txt:
the name a passer-by sees in a phone's network list, a joke that
implies a whole story in a few words. The ex took the dog and
left the router behind. Standard library only.
"""

import os

NETWORK_NAME = "MyExTookTheDogNotTheRouter"


def check_name(text):
    """Check the network name against the competition gate.

    The gate needs plain UTF-8 text of 1 to 32 characters, not only
    white space, on a single line: one Wi-Fi network name that lands
    a joke and hints at a story. Returns the cleaned text or raises
    ValueError.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("network name must not be only whitespace")
    if len(cleaned) > 32:
        raise ValueError(
            "network name is %d characters, over the 32 limit"
            % len(cleaned)
        )
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("network name must be exactly one line")
    return cleaned


def name_shape(text):
    """Measure the network name for one last sanity pass.

    Returns a dict with the character count and the word count of
    the cleaned text. A name too long to fit a phone's network
    list, or one padded out to fill the cap instead of landing
    the joke, is caught here before anything is written.
    """
    words = text.split()
    return {"chars": len(text), "words": len(words)}


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    text = check_name(NETWORK_NAME)
    shape = name_shape(text)
    if shape["chars"] < 1:
        raise ValueError("network name is empty")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
