#!/usr/bin/env python3
import os
import json
from pathlib import Path
import re
POSTS_DIR = Path("posts")
OUTPUT_FILE = POSTS_DIR / "posts.json"
# Matches files like 20251203.001.html
POST_PATTERN = re.compile(r"^(\d{8})\.(\d{3})\.html$")
def main():
    if not POSTS_DIR.exists():
        raise SystemExit("Error: 'posts/' directory not found.")
    posts = []
    for file in POSTS_DIR.iterdir():
        if file.is_file() and POST_PATTERN.match(file.name):
            posts.append(file.name)
    # Sort newest → oldest
    posts.sort(reverse=True)
    # Prepend "posts/" to each
    manifest = [f"posts/{name}" for name in posts]
    # Write json
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)
    print(f"Updated {OUTPUT_FILE} with {len(manifest)} entries.")
if __name__ == "__main__":
    main()
