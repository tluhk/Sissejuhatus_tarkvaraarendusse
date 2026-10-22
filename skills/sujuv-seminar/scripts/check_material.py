#!/usr/bin/env python3
"""Check a seminar's local Markdown links and basic Marp structure."""

import argparse
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit


def inspect(folder: Path) -> list[str]:
    errors = []
    if not folder.is_dir():
        return [f"Kausta ei leitud: {folder}"]
    slides = folder / "slides.md"
    if not slides.is_file():
        errors.append("Puudub slides.md")
    linked_chapters = set()
    link_pattern = re.compile(r"!?\[[^\]]*\]\((<[^>]+>|[^\s)]+)(?:\s+\"[^\"]*\")?\)")
    for file in sorted(folder.rglob("*.md")):
        text = file.read_text(encoding="utf-8")
        fence = None
        readable = []
        for line_number, line in enumerate(text.splitlines(), 1):
            marker = re.match(r"^\s{0,3}(`{3,}|~{3,})(.*)$", line)
            if marker:
                run, rest = marker.groups()
                if fence is None:
                    fence = (run[0], len(run), line_number)
                elif run[0] == fence[0] and len(run) >= fence[1] and not rest.strip():
                    fence = None
                continue
            if fence is None:
                readable.append(line)
        if fence:
            errors.append(f"{file}:{fence[2]}: sulgemata koodiplokk")
        for match in link_pattern.finditer("\n".join(readable)):
            raw = match.group(1).strip("<>")
            url = urlsplit(raw)
            if url.scheme or url.netloc:
                continue
            if not url.path:
                if raw.startswith("#"):
                    errors.append(f"{file}: kasuta faili linki pealkirjaankru asemel: {raw}")
                continue
            target = (file.parent / unquote(url.path)).resolve()
            if not target.exists():
                errors.append(f"{file}: puuduv lingisiht {raw}")
            if file == slides:
                linked_chapters.add(target)
    if slides.is_file():
        body = slides.read_text(encoding="utf-8")
        body = re.sub(r"\A---\s*\n.*?\n---\s*\n", "", body, count=1, flags=re.S)
        body = re.sub(r"<!--.*?-->", "", body, flags=re.S)
        parts = re.split(r"\n---[ \t]*\n", body)
        for index, part in enumerate(parts, 1):
            if not part.strip():
                errors.append(f"slides.md: tühi slaid {index}")
        for chapter in sorted((folder / "peatukid").rglob("*.md")):
            if chapter.resolve() not in linked_chapters:
                errors.append(f"Peatükk puudub slaidide linkidest: {chapter.name}")
        print(f"Slaide: {len(parts)}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("folder", type=Path, help="Seminari õppematerjali kaust")
    args = parser.parse_args()
    errors = inspect(args.folder.resolve())
    if errors:
        for error in errors:
            print(f"VIGA: {error}")
        return 1
    print("Kohalikud lingid, koodiplokid ja peatükkide leitavus on korras.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
