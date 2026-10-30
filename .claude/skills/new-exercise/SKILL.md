---
name: new-exercise
description: Create LeetCode practice stubs for my DSA sessions, one file per challenge, exercise body only, never the solution. Use when I say "new exercise", "/new-exercise" or "create the DSA files".
---

# New exercise

Create practice files for a DSA session. I solve them myself, so you NEVER write a solution, a partial solution or a hint in the code.

## 1. Ask me first (one message, short)

- Session number and topic (e.g. `02` and `two pointers`)
- Which LeetCode problems (numbers or names, one or more)

Wait for my answer. Do not guess the problems.

## 2. Where files go

- Folder per session: `src/NN_topic_name/` (two digits + snake_case), e.g. `src/02_two_pointers/`
- One file per challenge: `lcNNNN_problem_name.py` (4-digit LeetCode number + snake_case title), e.g. `lc0125_valid_palindrome.py`
- If a file already exists, stop and tell me. Never overwrite or edit my existing practice files.

## 3. File template

```python
"""LeetCode NNNN · Problem Title (Difficulty).

Session: DSA NN · Topic
Link: https://leetcode.com/problems/<slug>/

Problem:
<short restatement in your own words, 2 to 5 lines>

Constraints:
- <input size, value ranges, sorted or not, unique answer, etc.>
- Target: <expected time / space, e.g. O(n) time, O(1) extra space>

Think about:
- <one question that points at the pattern, no answer>
"""

def function_name(arg: type) -> return_type:
    raise NotImplementedError

if __name__ == "__main__":
    assert function_name(...) == ...
    assert function_name(...) == ...
    assert function_name(...) == ...  # edge case
    print("function_name ✅")
```

Rules for the template:
- Function name and signature match LeetCode, in snake_case, fully typed (`list[int]`, `dict[str, int]`, `str | None`). Pylance strict friendly.
- Body is only `raise NotImplementedError`.
- 2 to 4 asserts from the LeetCode examples plus 1 edge case. Expected values must be correct.
- Follow `.editorconfig`: 4-space indent, LF, UTF-8, final newline.
- Everything in English.

## 4. After creating

1. Run each new file once: `python3 src/NN_topic_name/lcNNNN_problem_name.py`. It must fail with `NotImplementedError`. That is expected.
2. Run `/update-docs` to list the session and its problems as "in progress" in `README.md` and `CLAUDE.md`. No solutions, no complexity yet.
3. Do not commit.
4. Reply with a short list: file paths + the run command for each.
