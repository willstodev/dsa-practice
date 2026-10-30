# DSA Practice

My personal practice of Data Structures & Algorithms in Python — solved by me while learning.

## Structure

```
src/
  NN_topic_name.py                  # older: one file per topic
  NN_topic_name/                    # current: one folder per session
    lcNNNN_problem_name.py          #   one file per LeetCode problem
README.md   # overview + progress
CLAUDE.md   # concept notes + rules
```

## How to run

```bash
python3 src/01_arrays_hashing/lc0001_two_sum.py
```

Each file runs its own `assert` tests and prints ✅ when they pass.

## Progress

| # | Topic | File | Problems | Key concept |
|---|---|---|---|---|
| 01 | Arrays & Hashing | [`src/01_arrays_hashing/`](src/01_arrays_hashing/) | Contains Duplicate, Two Sum | Hash set / hash map for O(1) lookups → O(n) solutions |

## Notes

A summary of every concept learned (approach, time/space complexity, patterns) lives in [`CLAUDE.md`](CLAUDE.md).
