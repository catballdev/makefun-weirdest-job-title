#!/usr/bin/env python3
"""
Read job title from line.txt and write to entry.txt in the output directory.

This script reads a job title from 'line.txt' (next to this script),
strips surrounding whitespace, and writes it to 'entry.txt' inside
the output directory specified by MAKEFUN_OUTPUT_DIR env var,
defaulting to /output. Creates the output directory if needed.

The output is deterministic: same input always produces identical bytes.
"""
import os


def main() -> None:
    """Read job title from line.txt and write to entry.txt in output directory."""
    # Read the job title from line.txt in the same directory as this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    line_txt_path = os.path.join(script_dir, "line.txt")

    with open(line_txt_path, "r", encoding="utf-8") as f:
        title = f.read().strip()

    # Determine output directory (default to /output if not set)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)

    # Write to entry.txt
    entry_txt_path = os.path.join(output_dir, "entry.txt")
    with open(entry_txt_path, "w", encoding="utf-8") as f:
        f.write(title)


if __name__ == "__main__":
    main()