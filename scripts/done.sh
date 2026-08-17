#!/usr/bin/env bash
# Usage: ./scripts/done.sh 12 "streams and Optional"
# Commits the day and reminds you to log it.
set -e
N=$(printf "%03d" "$1")
git add -A
git commit -m "day-$N: $2"
echo ""
echo "Committed day-$N."
echo "Now: 1) add the row to PROGRESS.md"
echo "     2) tick day $1 in runbook-180.html"
echo "     3) text your person: \"Day $1 done\""
