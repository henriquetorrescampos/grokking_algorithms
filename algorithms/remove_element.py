def remove_element(nums, val):
    k = 0
    for i in range(len(nums)):
        if nums[i] != val: # se nums[0] diferente de 5, 3 != 5
            nums[k] = nums[i]
            k += 1 #contador, conta o meu k que vai ser o meu output
    nums[:] = nums[:k] # [:] do inicio ate o final da array recebe a nova array de k de 0 ate o k
    return nums, k

n = 5
nums = [3, 5, 4, 1, 5, 2]

print(remove_element(nums, n))


# [3, 4, 1, 2]
"""
3 != 5 sim, nums[0] = nums[0], k=1
5 != 5 nao,
4 != 5, sim, nums[1] = nums[2], k=2
1 != 5, sim, nums[2] = nums[3], k=3
5 != 5, nao
2 != 5, sim, nums[3] = nums[5], k=4
"""
