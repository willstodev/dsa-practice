"""
LeetCode 0125 · Valid Palindrome (Easy).

Session: DSA 02 · Two Pointers
Link: https://leetcode.com/problems/valid-palindrome/

Problem:
Given a string s, return True if it reads the same forward and backward
after converting all uppercase letters to lowercase and removing every
non-alphanumeric character. Letters and digits both count as alphanumeric.

Constraints:
- 1 <= len(s) <= 2 * 10^5
- s contains only printable ASCII characters.
- Target: O(n) time, O(1) extra space.

Think about:
- Can you compare characters in place, without building a cleaned copy of the string?
"""

import re


def is_palindrome(s: str) -> bool:
    txt = re.sub(r"[^a-zA-Z0-9]", "", s).lower()
    i = len(txt) - 1
    res = ""

    while i >= 0:
        res += txt[i]
        i -= 1

    return txt == res


def is_palindrome_v2(s: str) -> bool:
    l = 0
    r = len(s) - 1

    while l < r:
        if not s[l].isalnum():
            l += 1
            continue

        if not s[r].isalnum():
            r -= 1
            continue

        if s[l].lower() != s[r].lower():
            return False

        l += 1
        r -= 1

    return True


if __name__ == "__main__":
    def it(description: str, actual: object, expected: object) -> None:
        assert actual == expected, f"✗ {description}: expected {expected!r}, got {actual!r}"
        print(f"  ✓ {description}")

    print("is_palindrome")
    it("ignores case and punctuation", is_palindrome("A man, a plan, a canal: Panama"), True)
    it("returns False when the cleaned text differs from its reverse", is_palindrome("race a car"), False)
    it("treats a string with no alphanumerics as a palindrome", is_palindrome(" "), True)
    it("counts digits as alphanumeric (\"0\" != \"p\")", is_palindrome("0P"), False)
    print("is_palindrome ✅")

    print("is_palindrome_v2")
    it("ignores case and punctuation", is_palindrome_v2("A man, a plan, a canal: Panama"), True)
    it("returns False on the first mismatched pair", is_palindrome_v2("race a car"), False)
    it("treats a string with no alphanumerics as a palindrome", is_palindrome_v2(" "), True)
    it("counts digits as alphanumeric (\"0\" != \"p\")", is_palindrome_v2("0P"), False)
    print("is_palindrome_v2 ✅")
