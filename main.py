#!/usr/bin/env python3
"""The Vacuum's Alibi — one-line entry writer.

Writes the exact 76-character entry to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt when set), no trailing newline.
Stdlib only, no network.
"""

import os

ENTRY = "That spot is scheduled for Thursday. Today is Tuesday. I do not do overtime."

EXPECTED_LEN = 76


def main() -> None:
    if not (1 <= len(ENTRY) <= 200):
        raise SystemExit(
            "entry length %d outside allowed range 1-200" % len(ENTRY)
        )
    if len(ENTRY) != EXPECTED_LEN:
        raise SystemExit(
            "entry length mismatch: got %d, expected %d" % (len(ENTRY), EXPECTED_LEN)
        )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip() or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = ENTRY.encode("utf-8")
    with open(path, "wb") as fh:
        fh.write(data)
    # Read-back verification: exact bytes, exact length.
    with open(path, "rb") as fh:
        back = fh.read()
    assert back == data, "read-back mismatch"
    assert len(back) == EXPECTED_LEN, "read-back length mismatch: %d" % len(back)
    print("wrote %s (%d bytes)" % (path, len(back)))


if __name__ == "__main__":
    main()
