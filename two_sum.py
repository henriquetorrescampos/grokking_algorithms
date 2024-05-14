def twoSum(nums, target):
    # first solution - brute force
    n = len(nums)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

nums = [11, 2, 5, 7]
target = 9
twoSum(nums, target)


