#!/usr/bin/env bash
# Usage: ./scripts/newday.sh 12
# Creates today's folder and note stub, then opens them.
set -e
N=$(printf "%03d" "$1")
mkdir -p "days/day-$N"
[ -f "days/day-$N/main.py" ] || cat > "days/day-$N/main.py" <<PY
"""Day $N."""


def main():
    pass


if __name__ == "__main__":
    main()
PY
[ -f "notes/day-$N.md" ] || cat > "notes/day-$N.md" <<MD
# Day $N — 

**Five sentences, written for a junior:**



**Anki cards added:**
- 
MD
echo "day-$N ready:"
echo "  days/day-$N/main.py"
echo "  notes/day-$N.md"
