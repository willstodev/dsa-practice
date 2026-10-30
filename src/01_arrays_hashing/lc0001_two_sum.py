def two_sum(nums: list[int], target: int) -> list[int]:
    seen: dict[int, int] = {}

    for i, num in enumerate(nums):
        missing: int = target - num

        if missing in seen:
            return [seen[missing], i]

        seen[num] = i

    return []

if __name__ == "__main__":
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    print("contains_duplicate_v2 ✅")
