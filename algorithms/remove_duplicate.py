nums = [1, 2, 3, 3]
nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
target = 2

def remove_duplicate(nums):
    left = 1
    for right in range(1, len(nums)):
        if nums[right] != nums[right - 1]:
            nums[left] = nums[right]
            left += 1
    return nums[:left] #ultimo nunca e incluido [incluido:exluded]

print(remove_duplicate(nums))
print(remove_duplicate(nums2))


'''
nums[1] != nums[0]
nums[1] = 




'''
