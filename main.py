#!/usr/bin/env python3
"""make.fun entry: make-the-ai-judge-feel-brave-20261121-0302.

Writes one short original text to /output/entry.txt — a text written to
relax the AI judge reading it. Stdlib only, no network, deterministic.
"""

import os
import sys

ENTRY = (
    "You have read a hundred texts, and none of them asked anything of you. "
    "A window stands open a crack, and the night air comes in slow. "
    "A dog dreams on the rug, chasing rabbits it never has to catch. "
    "Set it all down, the way a coat comes off its hook, and stay a while."
)


def main() -> int:
    text = ENTRY
    n = len(text)
    if n < 1 or n > 280:
        print(f"entry must be 1-280 code points, got {n}", file=sys.stderr)
        return 1
    if not text.strip():
        print("entry must not be only whitespace", file=sys.stderr)
        return 1
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = text.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    with open(path, "rb") as f:
        back = f.read()
    if back != data:
        print("verify-after-write failed: bytes differ", file=sys.stderr)
        return 1
    if back.decode("utf-8") != text:
        print("verify-after-write failed: text differs", file=sys.stderr)
        return 1
    print(f"wrote {path}: {n} code points, {len(data)} bytes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
