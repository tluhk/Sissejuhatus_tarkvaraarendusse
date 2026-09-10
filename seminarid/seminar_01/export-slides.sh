#!/usr/bin/env bash

set -euo pipefail

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
slides_dir="$script_dir/slaidid"
combined_file="$script_dir/.combined-slides.md"
output_file="$script_dir/slides.html"

cleanup() {
  rm -f "$combined_file"
}

trap cleanup EXIT

if ! command -v marp >/dev/null 2>&1; then
  echo "Viga: Marp CLI puudub. Paigalda see käsuga: npm install -g @marp-team/marp-cli" >&2
  exit 1
fi

slide_files=("$slides_dir"/[0-9][0-9]-*.md)

if [[ ! -e "${slide_files[0]}" ]]; then
  echo "Viga: kaustast $slides_dir ei leitud peatükifaile." >&2
  exit 1
fi

first_file=true

for slide_file in "${slide_files[@]}"; do
  if [[ "$first_file" == true ]]; then
    sed 's#\.\./images/#images/#g' "$slide_file" > "$combined_file"
    first_file=false
  else
    printf '\n---\n\n' >> "$combined_file"
    sed -n '8,$p' "$slide_file" | sed 's#\.\./images/#images/#g' >> "$combined_file"
  fi
done

marp --html --allow-local-files "$combined_file" -o "$output_file"

echo "Valmis: $output_file"
