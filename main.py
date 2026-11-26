import os
import sys


def main() -> int:
    """Write one honest line to my younger self."""
# Entry validated: output is 1-200 chars, one line, deterministic.
    LINE = "You stopped calling Marcus after his divorce because you didn't know what to say, and the silence you called respect became the loudest thing between you — he died wondering if you still cared."
    content = LINE + "\n"

    # Validation
    if not (1 <= len(content) <= 200 and content.strip()):
        raise ValueError("content must be 1-200 chars including newline, not only whitespace")
    if content.count("\n") != 1 or content.rstrip("\n").count("\n") != 0:
        raise ValueError("content must contain exactly one line")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)

    # Mirror to /output if different
    if os.path.abspath(out_dir) != os.path.abspath("/output"):
        try:
            os.makedirs("/output", exist_ok=True)
            with open("/output/entry.txt", "w", encoding="utf-8") as f:
                f.write(content)
        except Exception:
            pass

    print(f"{out_path} {len(content)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
