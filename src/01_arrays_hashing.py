def contains_duplicate(nums: list[int]) -> bool:
    seen: set[int] = set()

    for num in nums:
        if num in seen:
            return True
        
        seen.add(num)
        
    return False

def contains_duplicate_v2(nums: list[int]) -> bool:
    return len(set(nums)) != len(nums)


def two_sum(nums: list[int], target: int) -> list[int]:
    seen: dict[int, int] = {}

    for i, num in enumerate(nums):
        missing: int = target - num

        if missing in seen:
            return [seen[missing], i]

        seen[num] = i

    return []


if __name__ == "__main__":
    assert contains_duplicate([1, 2, 3, 1]) is True
    assert contains_duplicate([1, 2, 3]) is False
    print("contains_duplicate passed ✅")

    assert contains_duplicate_v2([1, 2, 3, 1]) is True
    assert contains_duplicate_v2([1, 2, 3]) is False
    print("contains_duplicate_v2 ✅")

    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    print("contains_duplicate_v2 ✅")
