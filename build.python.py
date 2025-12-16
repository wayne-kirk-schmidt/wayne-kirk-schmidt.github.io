#!/usr/bin/env python3

"""
Generate a web-facing JSON manifest of post files.
Filesystem paths are resolved internally; manifest entries are relative.
"""

import json
import re

import sys
sys.dont_write_bytecode = True

from pathlib import Path
from typing import List

BASE_DIR: Path = Path(__file__).resolve().parent
POSTS_DIR: Path = Path(f"{BASE_DIR}/posts").resolve()
OUTPUT_FILE: Path = Path(f"{POSTS_DIR}/posts.json")

# Matches files like 20251203.001.html
POST_PATTERN: re.Pattern[str] = re.compile(
    r"^(\d{8})\.(\d{3})\.html$"
)


def main() -> None:
    """
    Build a JSON manifest of post filenames found in POSTS_DIR.

    Scans for files matching POST_PATTERN, sorts them newest to oldest,
    and writes a list of relative paths to OUTPUT_FILE.

    Exits the program if POSTS_DIR does not exist.
    """
    if not POSTS_DIR.exists():
        raise SystemExit("Error: 'posts/' directory not found.")

    posts: List[str] = []

    for file in POSTS_DIR.iterdir():
        if file.is_file() and POST_PATTERN.match(file.name):
            posts.append(file.name)

    # Sort newest → oldest
    posts.sort(reverse=True)

    # Prepend "posts/" to each
    manifest: List[str] = [f"posts/{name}" for name in posts]

    # Confirm quality
    assert all(entry.startswith("posts/") for entry in manifest)

    # Count the manifest entries    
    entry_count: int = len(manifest)

    # Write JSON
    with open(OUTPUT_FILE, "w", encoding="utf-8") as manifestfile:
        json.dump(manifest, manifestfile, indent=2)

    print(f"Updated {OUTPUT_FILE} with {entry_count} entries.")


if __name__ == "__main__":
    main()
