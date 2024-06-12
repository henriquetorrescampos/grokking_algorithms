def remove_element(nums, val):
    k = 0
    for i in range(len(nums)):
        if nums[i] != val: # se nums[0] diferente de 5, 3 != 5
            nums[k] = nums[i]
            k += 1
    nums[:] = nums[:k] # [:] do inicio ate o final da array recebe a nova array de k de 0 ate o k
    return nums, k

n = 5
nums = [3, 5, 4, 1, 5, 2]

print(remove_element(nums, n))