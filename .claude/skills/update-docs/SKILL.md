---
name: update-docs
description: Update README.md and CLAUDE.md after a DSA practice file is created or changed, either a flat topic file (src/NN_topic.py) or a session folder of LeetCode files (src/NN_topic/lcNNNN_problem.py). Use when the user says "update docs", "document my new file", "I learned a new concept", or after adding a new practice file or session.
---

# Update DSA docs

Document new practice files in `README.md` and `CLAUDE.md`. **Never modify the practice files themselves.**

## Layouts

Two layouts live side by side in `src/`:

- **Flat topic file** (older): `src/NN_topic_name.py`, several problems in one file.
- **Session folder** (current): `src/NN_topic_name/`, one file per problem: `lcNNNN_problem_name.py`.

Both use the `NN` number for ordering. A session counts as one entry, whichever layout it uses.

## Steps

1. **Find what's new.** Run `git status --short` and `ls src/*.py src/*/*.py`. Compare the practice files (`src/NN_*.py` and `src/NN_*/lc*.py`) against the sections already in `CLAUDE.md` → "Concepts learned" and the README "Progress" table. If the user named a specific file or session, use that one.
2. **Read each new/changed file fully** (read only — no edits, no formatting, no "fixes").
3. **Check status.** Run each file with `python3 src/<file>` (or `python3 src/NN_topic_name/lcNNNN_problem_name.py`). Don't change anything based on the result.
   - Body is still only `raise NotImplementedError` → **in progress**.
   - Has a real implementation → **solved** (note in chat if its asserts fail).
4. **Update `CLAUDE.md`** — under "## Concepts learned", add (or update) one section per session, in number order:

   ```markdown
   ### NN — Topic Name (`src/NN_topic_name.py`)       ← flat file
   ### NN — Topic Name (`src/NN_topic_name/`)         ← session folder

   **Key idea:** one or two sentences on the core concept.

   | Problem | Approach | Time | Space |
   |---|---|---|---|
   | `function_name` | short plain-language explanation | O(?) | O(?) |

   **Patterns to remember:**
   - short, practical takeaways
   ```

   - One table row per function, including `_v2`/`_v3` variants (note how they differ).
   - Session folders: prefix the problem with its number, e.g. `` LC 0125 `is_palindrome` ``.
   - In-progress problems: write `⏳ in progress` in Approach and `—` for Time/Space. No hints, no solution, no complexity.
   - If every problem in the session is in progress, write `**Key idea:** ⏳ in progress` and leave out "Patterns to remember".
   - Describe the approach the user *actually wrote*, not a better one.
   - Complexities must match the user's code.
   - If the file introduces a new convention, add it to "Conventions in my practice files".
5. **Update `README.md`** — add/update one row per session in the "Progress" table (`# | Topic | File | Problems | Key concept`), keeping rows ordered by number.
   - File column links to the flat file (`src/<file>`) or the session folder (`src/NN_topic_name/`).
   - Use readable problem names (e.g. "Two Sum"); mark unsolved ones with ⏳.
   - Key concept is `⏳ in progress` until at least one problem is solved.
6. **Report back** in chat: what was documented, and any bugs, typos or wrong test outputs you noticed in the practice file — as suggestions only, with `file:line`. Let the user fix them.

## Rules

- Edit only `README.md` and `CLAUDE.md`.
- Keep the existing style and structure of both docs; keep it short.
- Follow `.editorconfig` (4 spaces, LF, UTF-8, final newline).
- Don't commit unless the user asks.
