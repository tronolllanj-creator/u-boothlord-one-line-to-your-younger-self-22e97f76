import os
import sys


def main() -> None:
    """Write one line to your younger self to entry.txt."""
# Entry validated: output is 1-200 chars, one line, deterministic.
    LINE = "You'll stay in that job years past its welcome just to say you didn't quit, and the bill comes due in the person you become while waiting — smaller, quieter, already replaced.\n"
    content = LINE

    if not (1 <= len(content) <= 200 and content.strip()):
        raise ValueError("content must be 1-200 chars including newline, not only whitespace, exactly one line")
    if content.count('\n') != 1 or not content.endswith('\n'):
        raise ValueError("content must contain exactly one line ending with newline")

    output_dir = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, 'entry.txt')

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)

    if output_dir != '/output':
        try:
            os.makedirs('/output', exist_ok=True)
            with open('/output/entry.txt', 'w', encoding='utf-8') as f:
                f.write(content)
        except Exception:
            pass

    print(f"{output_path} {len(content)}")


if __name__ == '__main__':
    main()
