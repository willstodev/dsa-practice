"""
LeetCode 0167 · Two Sum II - Input Array Is Sorted (Medium).

Session: DSA 02 · Two Pointers
Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

Problem:
Given a 1-indexed list of integers sorted in non-decreasing order, find the
two numbers that add up to target. Return their indices as [index1, index2]
(1-indexed, index1 < index2). The same element cannot be used twice.

Constraints:
- 2 <= len(numbers) <= 3 * 10^4
- -1000 <= numbers[i] <= 1000, sorted in non-decreasing order
- -1000 <= target <= 1000
- Exactly one solution exists.
- Target: O(n) time, O(1) extra space.

Think about:
- What does the sorted order tell you when a pair's sum is too small or too large?
"""

def two_sum(numbers: list[int], target: int) -> list[int]:
    left = 0
    right = len(numbers) - 1

    while left < right:
        result = numbers[left] + numbers[right]
        if result == target:
            return [left + 1, right + 1]
        elif result > target:
            right -= 1
        else:
            left += 1

    return []


if __name__ == "__main__":
    def it(description: str, actual: object, expected: object) -> None:
        assert actual == expected, f"✗ {description}: expected {expected!r}, got {actual!r}"
        print(f"  ✓ {description}")

    print("two_sum")
    it("returns 1-indexed positions of the pair", two_sum([2, 7, 11, 15], 9), [1, 2])
    it("finds a pair that is not adjacent", two_sum([2, 3, 4], 6), [1, 3])
    it("works with negative numbers", two_sum([-1, 0], -1), [1, 2])
    it("handles duplicate values without reusing one element", two_sum([1, 2, 3, 3], 6), [3, 4])
    print("two_sum ✅")
