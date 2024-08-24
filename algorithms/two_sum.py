# def twoSum(nums, target):
#     # first solution - brute force, O(n**2)
#     n = len(nums)
#     for i in range(n - 1):
#         for j in range(i + 1, n):
#             if nums[i] + nums[j] == target:
#                 return [i, j]
#     return []

# nums = [11, 2, 5, 7]
# target = 9
# twoSum(nums, target)

def two_sum(nums, target):
    dict = {}
    for index, value in enumerate(nums):
        difference = target - value # 5 - 2 = 3, 5 - 3 = 2
        if difference in dict: # se diferente estiver em dict 
            # print([dict[difference]]) # chamo o [dicionario[key]] pego valor {4: 2}, pego o valor 2
            return [dict[difference], index]
        else:
            dict[value] = index # dict[2] = 0, {2: 0} / dict[3] = 1, {3: 1} / dict[4] = 2 {4: 2}


print(two_sum([2, 3, 4, 4], 8))