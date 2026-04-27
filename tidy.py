#!/usr/bin/env python3
"""
tidy.py — Move CPH-created solution files from root into contests/<group>/,
using the "group" field from .cph metadata to organize by contest.

CPH stores metadata in:  .cph/.<filename>_<md5(srcPath)>.prob
The JSON inside contains:
  - "srcPath": absolute path to the source file
  - "group":   e.g. "Codeforces - Codeforces Beta Round 4 (Div. 2 Only)"

When we move the .py, we:
  1. Read the .prob to get the group name
  2. Sanitize group into a folder name
  3. Move the .py to contests/<group>/
  4. Move the .prob from root .cph/ to contests/<group>/.cph/ with updated srcPath
  5. Remove root .cph/ if empty after all moves
"""

import hashlib
import json
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).parent
CPH_DIR = ROOT / ".cph"
CONTESTS_DIR = ROOT / "contests"

# Files in root that are NOT solutions
SKIP = {
    "tidy.py",
    "Makefile",
    "pyproject.toml",
    "README.md",
    ".gitignore",
    ".python-version",
}


def md5(s: str) -> str:
    return hashlib.md5(s.encode()).hexdigest()


def sanitize_folder_name(group: str) -> str:
    """
    Turn a CPH group string into a clean folder name.

    "Codeforces - Codeforces Beta Round 4 (Div. 2 Only)"
      → "Codeforces_Beta_Round_4_Div_2_Only"

    "CSES - CSES Problem Set"
      → "CSES_Problem_Set"

    "AtCoder - AtCoder Beginner Contest 350"
      → "AtCoder_Beginner_Contest_350"
    """
    # Strip the "Judge - " prefix if duplicated in the name
    # e.g. "Codeforces - Codeforces Beta..." → "Codeforces Beta..."
    if " - " in group:
        prefix, rest = group.split(" - ", 1)
        if rest.startswith(prefix):
            group = rest
        else:
            group = rest

    # Remove special characters, keep alphanumeric and spaces
    group = re.sub(r"[^\w\s-]", "", group)
    # Collapse whitespace into single underscore
    group = re.sub(r"\s+", "_", group.strip())
    # Collapse multiple underscores
    group = re.sub(r"_+", "_", group)

    return group or "ungrouped"


def find_prob_file(filename: str) -> Path | None:
    """Find the .cph metadata file matching a source filename."""
    if not CPH_DIR.exists():
        return None
    prefix = f".{filename}_"
    for f in CPH_DIR.iterdir():
        if f.name.startswith(prefix):
            return f
    return None


def read_prob_data(prob_file: Path | None) -> dict | None:
    """Read and parse the .prob JSON, or return None."""
    if prob_file is None:
        return None
    try:
        return json.loads(prob_file.read_text())
    except (json.JSONDecodeError, OSError):
        return None


def move_solution(py_file: Path) -> bool:
    """Move a .py from root to contests/<group>/ and copy CPH metadata."""
    prob_file = find_prob_file(py_file.name)
    prob_data = read_prob_data(prob_file)

    # Determine destination folder
    if prob_data and "group" in prob_data:
        group_folder = sanitize_folder_name(prob_data["group"])
    else:
        group_folder = "ungrouped"

    dest_dir = CONTESTS_DIR / group_folder
    dest = dest_dir / py_file.name

    if dest.exists():
        print(f"  ⚠ {dest.relative_to(ROOT)} already exists, skipping")
        return False

    dest_dir.mkdir(parents=True, exist_ok=True)
    new_src_path = str(dest.resolve())

    # Move the .py file
    shutil.move(str(py_file), str(dest))

    # Copy updated .cph metadata to the destination
    if prob_data and prob_file:
        try:
            prob_data["srcPath"] = new_src_path

            # Write to contests/<group>/.cph/
            dest_cph = dest_dir / ".cph"
            dest_cph.mkdir(exist_ok=True)

            new_hash = md5(new_src_path)
            ext = prob_file.suffix
            new_prob_name = f".{py_file.name}_{new_hash}{ext}"
            new_prob_path = dest_cph / new_prob_name

            new_prob_path.write_text(json.dumps(prob_data, indent=2))

            # Remove the original from root .cph/ now that it's safely copied
            prob_file.unlink()

            rel = dest.relative_to(ROOT)
            print(f"  → {rel}  (metadata moved)")
        except (json.JSONDecodeError, KeyError, OSError) as e:
            rel = dest.relative_to(ROOT)
            print(f"  → {rel}  (metadata error: {e})")
    else:
        rel = dest.relative_to(ROOT)
        print(f"  → {rel}  (no metadata found)")

    return True


def main():
    CONTESTS_DIR.mkdir(exist_ok=True)

    # Find all .py files in root (not in subdirectories)
    solutions = [f for f in ROOT.iterdir() if f.suffix == ".py" and f.is_file() and f.name not in SKIP]

    if not solutions:
        print("nothing to move")
        return

    count = 0
    for f in sorted(solutions):
        if move_solution(f):
            count += 1

    print(f"✓ moved {count} file(s)")

    # Clean up root .cph/ if empty
    if CPH_DIR.exists() and not any(CPH_DIR.iterdir()):
        CPH_DIR.rmdir()
        print("  cleaned up empty .cph/")


if __name__ == "__main__":
    main()
