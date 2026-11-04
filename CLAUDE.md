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
    - **Flat topic file** (older): `src/NN_topic_name.py`, several problems in one file.
    - **Session folder** (current, created by `/new-exercise`): `src/NN_topic_name/`, one file per LeetCode problem named `lcNNNN_problem_name.py` (4-digit number + snake_case title), e.g. `src/01_arrays_hashing/lc0001_two_sum.py`.
- Session-folder files start with a docstring (problem, constraints, target complexity, "think about") and a stub body `raise NotImplementedError` until I solve it.
- One function per problem, with type hints (`list[int]`, `dict[int, int]`, ...).
- Alternative solutions use a `_v2`, `_v3` suffix.
- Tests live in `if __name__ == "__main__":`, Jest-style: a small `it(description, actual, expected)` helper that asserts and prints `✓ description`, one `it(...)` per case, then `print("... ✅")`.
- Run a file with: `python3 src/NN_topic_name.py` or `python3 src/NN_topic_name/lcNNNN_problem_name.py`

## Concepts learned

### 01 — Arrays & Hashing (`src/01_arrays_hashing/`)

**Key idea:** trade memory for speed — a hash set/map gives O(1) average lookup, turning O(n²) "compare everything" into a single O(n) pass.

| Problem | Approach | Time | Space |
|---|---|---|---|
| LC 0217 `contains_duplicate` | Walk the list, keep a `set` of seen numbers; return `True` on the first repeat (early exit). | O(n) | O(n) |
| LC 0217 `contains_duplicate_v2` | `len(set(nums)) != len(nums)` — one-liner, but always processes the whole list (no early exit). | O(n) | O(n) |
| LC 0001 `two_sum` | Walk the list, store `value -> index` in a `dict`; for each `num` check if its complement `target - num` was already seen. | O(n) | O(n) |

**Patterns to remember:**
- "Have I seen this before?" → `set`.
- "Where did I see it?" / need an index → `dict` (value → index).
- Check the dict *before* inserting the current element, so an element is never paired with itself.

### 02 — Two Pointers (`src/02_two_pointers/`)

**Key idea:** walk the sequence from both ends toward the middle; a palindrome check compares the start against the end, and on a sorted list the sum of the two ends tells you which pointer to move.

| Problem | Approach | Time | Space |
|---|---|---|---|
| LC 0125 `is_palindrome` | Clean with `re.sub(r"[^a-zA-Z0-9]", "", s).lower()`, build the reversed string with a backward index (`res += txt[i]`), then compare `txt == res`. | O(n)* | O(n) |
| LC 0125 `is_palindrome_v2` | Two pointers `l`/`r` on the original string: skip non-alphanumerics with `isalnum()` + `continue`, compare `s[l].lower() != s[r].lower()`, move both inward. No cleaned copy. | O(n) | O(1) |
| LC 0167 `two_sum` | Pointers `left`/`right` at both ends of the sorted list; if the sum equals `target` return `[left + 1, right + 1]` (1-indexed), if it's too big move `right -= 1`, if too small move `left += 1`. | O(n) | O(1) |

\* `str +=` in a loop is O(n²) in theory; CPython usually optimizes it to O(n) in practice.

**Patterns to remember:**
- Normalize first (filter non-alphanumeric + lowercase), then compare.
- `[^a-zA-Z0-9]` keeps digits too — `"0P"` is not a palindrome.
- Reversed copy = O(n) extra space; the O(1) version compares two indices (`l`, `r`) in place.
- Skip-and-`continue` keeps the loop simple: move only the pointer that's on junk, then re-check `l < r`.
- Early exit: return `False` on the first mismatch.
- Sorted input + pair sum → two pointers instead of a hash map: sum too big → `right -= 1`, too small → `left += 1`. O(1) space vs O(n) for LC 0001.
- Watch the indexing the problem asks for (LC 0167 is 1-indexed → `+ 1`).

### 03 — Sliding Window (`src/03_sliding_window/`)

**Key idea:** keep a window `[left, right]` over the list and move its edges in a single pass; `left` only jumps forward when a better start appears, so each element is visited once.

| Problem | Approach | Time | Space |
|---|---|---|---|
| LC 0121 `max_profit` | `left` = buy day, `right` = sell day (via `enumerate`). Each step updates `best = max(best, sell - buy)`; if `sell <= buy`, a new lowest price was found → move `left = right`. | O(n) | O(1) |

**Patterns to remember:**
- "Best pair where one comes before the other" → keep the best *start* so far and test every *end* against it.
- Move `left` straight to `right` when the current price is a new low — no earlier day can beat it.
- Start `best = 0` so "no profit possible" naturally returns 0.
