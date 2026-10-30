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
    def it(description: str, actual: object, expected: object) -> None:
        assert actual == expected, f"✗ {description}: expected {expected!r}, got {actual!r}"
        print(f"  ✓ {description}")

    print("contains_duplicate")
    it("returns True when a number repeats", contains_duplicate([1, 2, 3, 1]), True)
    it("returns False when all numbers are distinct", contains_duplicate([1, 2, 3]), False)
    it("returns True when many numbers repeat", contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]), True)
    it("returns False for a single element", contains_duplicate([1]), False)
    print("contains_duplicate ✅")

    print("contains_duplicate_v2")
    it("returns True when a number repeats", contains_duplicate_v2([1, 2, 3, 1]), True)
    it("returns False when all numbers are distinct", contains_duplicate_v2([1, 2, 3]), False)
    it("returns True when many numbers repeat", contains_duplicate_v2([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]), True)
    it("returns False for a single element", contains_duplicate_v2([1]), False)
    print("contains_duplicate_v2 ✅")
