#!/usr/bin/env bash

set -euo pipefail

if [[ $# -eq 0 ]]; then
  seminar_dirs=(
    "seminarid/seminar_02"
    "seminarid/seminar_03"
    "seminarid/seminar_04"
    "seminarid/seminar_05"
  )
else
  seminar_dirs=("$@")
fi

if ! command -v marp >/dev/null 2>&1; then
  echo "Viga: Marp CLI puudub. Paigalda: npm install -g @marp-team/marp-cli" >&2
  exit 1
fi

for seminar_dir in "${seminar_dirs[@]}"; do
  source_file="$seminar_dir/slides.md"
  output_file="$seminar_dir/slides.html"

  if [[ ! -f "$source_file" ]]; then
    echo "Viga: faili $source_file ei leitud." >&2
    exit 1
  fi

  marp --html --allow-local-files "$source_file" -o "$output_file"
  echo "Valmis: $output_file"
done
