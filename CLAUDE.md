# CLAUDE.md

This repo is my personal DSA (Data Structures & Algorithms) practice folder, written in Python.

## Rules (read first)

- **Never edit, refactor, "fix" or reformat my practice files** (`src/NN_topic.py` and `src/NN_topic/lcNNNN_*.py`). They are for learning — mistakes included. If you spot a bug, *tell me* in chat instead of changing the code.
- Only touch documentation files: `README.md` and `CLAUDE.md`.
- Don't create new practice files or solutions unless I explicitly ask. `/new-exercise` creates empty stubs only (never solutions).
- After I add a new practice file, run the `/update-docs` skill to document it.
- Follow `.editorconfig`: 4-space indent, LF line endings, UTF-8, final newline.

## Conventions in my practice files

- Practice files live in `src/`. Two layouts, both numbered `NN` (two-digit order + topic in snake_case):
    - **Flat topic file** (older): `src/NN_topic_name.py`, several problems in one file, e.g. `01_arrays_hashing.py`.
    - **Session folder** (current, created by `/new-exercise`): `src/NN_topic_name/`, one file per LeetCode problem named `lcNNNN_problem_name.py` (4-digit number + snake_case title), e.g. `src/02_two_pointers/lc0125_valid_palindrome.py`.
- Session-folder files start with a docstring (problem, constraints, target complexity, "think about") and a stub body `raise NotImplementedError` until I solve it.
- One function per problem, with type hints (`list[int]`, `dict[int, int]`, ...).
- Alternative solutions use a `_v2`, `_v3` suffix.
- Tests live in `if __name__ == "__main__":` as plain `assert`s plus a `print("... ✅")`.
- Run a file with: `python3 src/NN_topic_name.py` or `python3 src/NN_topic_name/lcNNNN_problem_name.py`

## Concepts learned

### 01 — Arrays & Hashing (`src/01_arrays_hashing.py`)

**Key idea:** trade memory for speed — a hash set/map gives O(1) average lookup, turning O(n²) "compare everything" into a single O(n) pass.

| Problem | Approach | Time | Space |
|---|---|---|---|
| `contains_duplicate` | Walk the list, keep a `set` of seen numbers; return `True` on the first repeat (early exit). | O(n) | O(n) |
| `contains_duplicate_v2` | `len(set(nums)) != len(nums)` — one-liner, but always processes the whole list (no early exit). | O(n) | O(n) |
| `two_sum` | Walk the list, store `value -> index` in a `dict`; for each `num` check if its complement `target - num` was already seen. | O(n) | O(n) |

**Patterns to remember:**
- "Have I seen this before?" → `set`.
- "Where did I see it?" / need an index → `dict` (value → index).
- Check the dict *before* inserting the current element, so an element is never paired with itself.
