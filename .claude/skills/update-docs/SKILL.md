---
name: update-docs
description: Update README.md and CLAUDE.md after a new DSA practice file (src/NN_topic.py) is created or changed. Use when the user says "update docs", "document my new file", "I learned a new concept", or after adding a new practice file.
---

# Update DSA docs

Document new practice files in `README.md` and `CLAUDE.md`. **Never modify the practice files themselves.**

## Steps

1. **Find what's new.** Run `git status --short` and `ls src/*.py`. Compare the practice files (`src/NN_*.py`) against the sections already in `CLAUDE.md` → "Concepts learned" and the README "Progress" table. If the user named a specific file, use that one.
2. **Read each new/changed file fully** (read only — no edits, no formatting, no "fixes").
3. **Optionally run it** with `python3 src/<file>` to see whether the tests pass. Don't change anything based on the result.
4. **Update `CLAUDE.md`** — under "## Concepts learned", add (or update) a section in file-number order:

   ```markdown
   ### NN — Topic Name (`src/NN_topic_name.py`)

   **Key idea:** one or two sentences on the core concept.

   | Problem | Approach | Time | Space |
   |---|---|---|---|
   | `function_name` | short plain-language explanation | O(?) | O(?) |

   **Patterns to remember:**
   - short, practical takeaways
   ```

   - One table row per function, including `_v2`/`_v3` variants (note how they differ).
   - Describe the approach the user *actually wrote*, not a better one.
   - Complexities must match the user's code.
   - If the file introduces a new convention, add it to "Conventions in my practice files".
5. **Update `README.md`** — add/update one row in the "Progress" table (`# | Topic | File | Problems | Key concept`, linking to `src/<file>`), keeping rows ordered by number. Use readable problem names (e.g. "Two Sum").
6. **Report back** in chat: what was documented, and any bugs, typos or wrong test outputs you noticed in the practice file — as suggestions only, with `file:line`. Let the user fix them.

## Rules

- Edit only `README.md` and `CLAUDE.md`.
- Keep the existing style and structure of both docs; keep it short.
- Follow `.editorconfig` (4 spaces, LF, UTF-8, final newline).
- Don't commit unless the user asks.
