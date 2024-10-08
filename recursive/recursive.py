"""
-- Recursive function --
When writing a recursive function that involvs an array, base-case will be many times 
either an empty array or an array with one element"""
    
def sum(nums):
    """Recursive function to sum all the values inside the list"""
    if nums == []:
        return 0
    else:
        return nums[0] + sum(nums[1:])

# print(sum([1, 2, 3]))

def highest_value(nums):
    if len(nums) == 2:
        return nums[0] if nums[0] > nums[1] else nums[1]
    else:
        num_higher = highest_value(nums[1:])
        return nums[0] if nums[0] > num_higher else num_higher

print(highest_value([2, 3, 4, 9]))


def EvenNums(num, even=None):
    if even is None: # base case for start list
        even = []
    if num <= 0: # base case ending recursion
        return even
    if num % 2 == 0:
        even.append(num)  
    return EvenNums(num - 1, even)

print(EvenNums(5))
