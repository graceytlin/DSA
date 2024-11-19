def two_sum(nums: list[int], target: int) -> list[int]:
    nums.sort()
    l, r = 0, len(nums) - 1

    while l < r:
        total = nums[l] + nums[r]

        if total > target:
            r -= 1
        elif total < target:
            l += 1
        else:
            return [l, r]