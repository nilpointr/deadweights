#!/usr/bin/env python3
"""deadweights — curriculum progress CLI"""

import argparse
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).parent
CURRICULUM = ROOT / "tiny-transformer-curriculum.md"
TEMPLATE = ROOT / "curriculum-template.md"

PHASE_RE = re.compile(r"^## (Phase \d+ — [^\n]+)", re.MULTILINE)
CHECKBOX_RE = re.compile(r"^- \[([ x])\]", re.MULTILINE)
NOTES_HEADER = "## Notes / Things That Were Confusing"


def read():
    return CURRICULUM.read_text()


def write(text):
    CURRICULUM.write_text(text)


def get_phases(text):
    matches = list(PHASE_RE.finditer(text))
    result = []
    for i, m in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        result.append((m.group(1), m.start(), end))
    return result


def phase_num(title):
    return int(re.search(r"\d+", title).group())


def item_label(line):
    label = re.sub(r"^- \[[ x]\] \*?\*?", "", line)
    label = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", label)
    label = re.sub(r"\*+", "", label)
    label = re.sub(r"^\(Optional[^)]*\)\s*", "", label)
    label = re.sub(r"\([^)]*\)", "", label)
    return label.strip()[:65]


def cmd_progress(args):
    text = read()
    phases = get_phases(text)

    if args.phase is not None:
        phase_map = {phase_num(t): (t, s, e) for t, s, e in phases}
        if args.phase not in phase_map:
            sys.exit(f"No Phase {args.phase} found.")
        title, start, end = phase_map[args.phase]
        chunk = text[start:end]
        print(f"\n{title}\n")
        for i, m in enumerate(CHECKBOX_RE.finditer(chunk), 1):
            state = m.group(1)
            line = chunk[m.start() : chunk.find("\n", m.start())]
            print(f"  {i}. [{'x' if state == 'x' else ' '}] {item_label(line)}")
        print()
        return

    print()
    total_done = total_all = 0
    for title, start, end in phases:
        chunk = text[start:end]
        items = list(CHECKBOX_RE.finditer(chunk))
        done = sum(1 for m in items if m.group(1) == "x")
        total = len(items)
        total_done += done
        total_all += total
        bar = "█" * done + "░" * (total - done)
        short = re.sub(r" \(skip.*", "", title)
        print(f"  {short:<48} {bar}  {done}/{total}")

    print(f"  {'─' * 58}")
    print(f"  {'Total':<48} {total_done}/{total_all}")
    print(f"\n  Tip: python3 dw.py progress <phase> to list items.\n")


def cmd_check(args):
    text = read()
    phases = get_phases(text)
    phase_map = {phase_num(t): (t, s, e) for t, s, e in phases}

    if args.phase not in phase_map:
        sys.exit(f"No Phase {args.phase} found.")

    _, start, end = phase_map[args.phase]
    chunk = text[start:end]
    items = list(CHECKBOX_RE.finditer(chunk))

    if args.item < 1 or args.item > len(items):
        sys.exit(f"Phase {args.phase} has {len(items)} item(s). Pick 1–{len(items)}.")

    m = items[args.item - 1]
    abs_pos = start + m.start(1)
    write(text[:abs_pos] + "x" + text[abs_pos + 1 :])

    line = chunk[m.start() : chunk.find("\n", m.start())]
    print(f"✓ Phase {args.phase}, item {args.item}: {item_label(line)}")


def cmd_note(args):
    text = read()
    pos = text.find(NOTES_HEADER)
    if pos == -1:
        sys.exit("Notes section not found in curriculum.")

    notes_section = text[pos:]
    empty = re.search(r"\n-\s*$", notes_section)
    if empty:
        abs_pos = pos + empty.start()
        new_text = (
            text[:abs_pos]
            + f"\n- {args.text.strip()}"
            + text[abs_pos + len(empty.group()) :]
        )
    else:
        new_text = text.rstrip() + f"\n- {args.text.strip()}\n"

    write(new_text)
    print("Note added.")


def cmd_define(args):
    text = read()
    pattern = re.compile(r"(\| " + re.escape(args.term) + r" \| )\|", re.IGNORECASE)
    if not pattern.search(text):
        sys.exit(f'"{args.term}" not found in glossary or already defined.')
    write(pattern.sub(rf"\g<1>{args.definition.strip()} |", text))
    print(f'Defined "{args.term}".')


def cmd_reset(_args):
    if not TEMPLATE.exists():
        sys.exit("curriculum-template.md not found.")
    confirm = input("Reset curriculum to template? This overwrites your progress. [y/N] ")
    if confirm.strip().lower() != "y":
        print("Aborted.")
        return
    shutil.copy(TEMPLATE, CURRICULUM)
    print("Curriculum reset.")


def main():
    parser = argparse.ArgumentParser(prog="dw", description="deadweights curriculum CLI")
    sub = parser.add_subparsers(dest="command", required=True)

    p_prog = sub.add_parser("progress", help="Show completion by phase")
    p_prog.add_argument("phase", nargs="?", type=int, help="Phase number for item detail")

    p_check = sub.add_parser("check", help="Mark an item complete")
    p_check.add_argument("phase", type=int, help="Phase number (0–4)")
    p_check.add_argument("item", type=int, help="Item number within phase (see: progress <phase>)")

    p_note = sub.add_parser("note", help="Append a note to the curriculum")
    p_note.add_argument("text", help="Note text (wrap in quotes)")

    p_define = sub.add_parser("define", help="Fill in a glossary term")
    p_define.add_argument("term", help='Term name, e.g. "Token"')
    p_define.add_argument("definition", help="Your one-line definition (wrap in quotes)")

    sub.add_parser("reset", help="Restore curriculum from template (prompts for confirmation)")

    args = parser.parse_args()
    {
        "progress": cmd_progress,
        "check": cmd_check,
        "note": cmd_note,
        "define": cmd_define,
        "reset": cmd_reset,
    }[args.command](args)


if __name__ == "__main__":
    main()
