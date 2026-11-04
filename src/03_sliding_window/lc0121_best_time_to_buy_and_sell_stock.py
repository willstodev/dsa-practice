"""
LeetCode 0121 · Best Time to Buy and Sell Stock (Easy).

Session: DSA 03 · Sliding Window
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Problem:
Given a list where prices[i] is a stock's price on day i, pick one day to buy
and a later day to sell. Return the maximum profit you can make. If no profit
is possible, return 0.

Constraints:
- 1 <= len(prices) <= 10^5
- 0 <= prices[i] <= 10^4
- You must buy before you sell (one transaction only).
- Target: O(n) time, O(1) extra space.

Think about:
- For each day you could sell on, which earlier day would you have wanted to buy on?
"""


def max_profit(prices: list[int]) -> int:
    left = 0
    best = 0

    for right, sell in enumerate(prices):
        buy = prices[left]
        best = max(best, sell - buy)

        if sell <= buy:
            left = right

    return best


if __name__ == "__main__":
    def it(description: str, actual: object, expected: object) -> None:
        assert actual == expected, f"✗ {description}: expected {expected!r}, got {actual!r}"
        print(f"  ✓ {description}")

    print("max_profit")
    it("returns the best profit from one buy and a later sell", max_profit([7, 1, 5, 3, 6, 4]), 5)
    it("returns 0 when prices only go down", max_profit([7, 6, 4, 3, 1]), 0)
    it("does not sell before buying", max_profit([2, 4, 1]), 2)
    it("returns 0 for a single day", max_profit([5]), 0)
    it("returns 0 when every price is the same", max_profit([3, 3, 3]), 0)
    it("keeps the best trade when a new low comes later", max_profit([3, 8, 1, 4]), 5)
    print("max_profit ✅")
