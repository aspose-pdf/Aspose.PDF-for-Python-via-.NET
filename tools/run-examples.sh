#!/usr/bin/env bash

find . -type f -name "example_*.py" -print0 |
while IFS= read -r -d '' file; do
  echo "Running $file"
  python "$file"
done
