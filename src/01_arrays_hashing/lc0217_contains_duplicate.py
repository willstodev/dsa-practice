def contains_duplicate(nums: list[int]) -> bool:
    seen: set[int] = set()

    for num in nums:
        if num in seen:
            return True
        
        seen.add(num)
        
    return False

def contains_duplicate_v2(nums: list[int]) -> bool:
    return len(set(nums)) != len(nums)

if __name__ == "__main__":
    assert contains_duplicate([1, 2, 3, 1]) is True
    assert contains_duplicate([1, 2, 3]) is False
    print("contains_duplicate passed ✅")

    assert contains_duplicate_v2([1, 2, 3, 1]) is True
    assert contains_duplicate_v2([1, 2, 3]) is False
    print("contains_duplicate_v2 ✅")
