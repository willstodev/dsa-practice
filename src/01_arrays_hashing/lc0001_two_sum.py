def two_sum(nums: list[int], target: int) -> list[int]:
    seen: dict[int, int] = {}

    for i, num in enumerate(nums):
        missing: int = target - num

        if missing in seen:
            return [seen[missing], i]

        seen[num] = i

    return []

if __name__ == "__main__":
    def it(description: str, actual: object, expected: object) -> None:
        assert actual == expected, f"✗ {description}: expected {expected!r}, got {actual!r}"
        print(f"  ✓ {description}")

    print("two_sum")
    it("finds the pair at the start of the list", two_sum([2, 7, 11, 15], 9), [0, 1])
    it("finds a pair that is not at the start", two_sum([3, 2, 4], 6), [1, 2])
    it("handles a pair of equal numbers", two_sum([3, 3], 6), [0, 1])
    it("works with negative numbers", two_sum([-1, -2, -3, -4, -5], -8), [2, 4])
    print("two_sum ✅")
