#!/usr/bin/env sh
# Rebuild the distributable zip (Claude Code .skill packaging). Other runtimes copy the directory.
set -eu
cd "$(dirname "$0")/.."
rm -f genealogy-research.skill
zip -qr genealogy-research.skill SKILL.md references scripts/gedcom_check.py
unzip -l genealogy-research.skill | tail -1
