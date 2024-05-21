def remove_element(nums, val):
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    nums[:] = nums[:k]
    return nums, k

val = 5
nums = [3, 5, 4, 1, 5, 2]

print(remove_element(nums, val))