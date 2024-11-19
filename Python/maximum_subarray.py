def max_subarray(nums):
    max_sub, cur_sum = nums[0], 0

    for num in nums:
        if cur_sum < 0:
            cur_sum = 0

        cur_sum += num
        max_sub = max(max_sub, cur_sum)

    return max_sub
