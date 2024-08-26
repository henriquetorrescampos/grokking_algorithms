nums = [1, 1, 3, 3]
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

s = 'abbaca'
string_to_list = []

for i in range(len(s)):
    if len(string_to_list) > 0 and string_to_list[-1] == s[i]:
        string_to_list.pop()
    else:
        string_to_list.append(s[i])

output = ''.join(string_to_list)
print(output)

