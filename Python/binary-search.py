# Given an array of distinct integers nums, sorted in ascending order, and an integer target
# Implement a function to search for target within nums. If it exists, then return its index, otherwise, return -1

def search(nums: list[int], target: int) -> int:
    l, r = 0, len(nums)-1

    while (l <= r):
        m = int(l+((r-l)/2))

        if (nums[m] == target):
            return m
        elif (nums[m] < target):
            l += 1
        else:
            r -= 1

    return -1

print(search([5],5))