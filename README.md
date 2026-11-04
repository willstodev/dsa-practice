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

Each file runs its own tests, Jest-style: one `✓ description` line per case, then ✅ when they all pass.

## Progress

| # | Topic | File | Problems | Key concept |
|---|---|---|---|---|
| 01 | Arrays & Hashing | [`src/01_arrays_hashing/`](src/01_arrays_hashing/) | Contains Duplicate, Two Sum | Hash set / hash map for O(1) lookups → O(n) solutions |
| 02 | Two Pointers | [`src/02_two_pointers/`](src/02_two_pointers/) | Valid Palindrome, Two Sum II | Left/right pointers moving inward → O(n) time, O(1) space |
| 03 | Sliding Window | [`src/03_sliding_window/`](src/03_sliding_window/) | Best Time to Buy and Sell Stock | Window `left`/`right` moving forward in one pass → O(n) time, O(1) space |

## Notes

A summary of every concept learned (approach, time/space complexity, patterns) lives in [`CLAUDE.md`](CLAUDE.md).
