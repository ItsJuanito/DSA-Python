
'''
Problem Statement:
We are given an array containing ‘n’ objects. Each object, when created, was assigned a 
unique number from 1 to ‘n’ based on their creation sequence. This means that the object 
with sequence number ‘3’ was created just before the object with sequence number ‘4’. 
Write a function to sort the objects in-place on their creation sequence number in O(n) 
and without any extra space. For simplicity, let’s assume we are passed an integer array 
containing only the sequence numbers, though each number is actually an object.

Example 1:
Input: [3, 1, 5, 4, 2]
Output: [1, 2, 3, 4, 5]
Explanation: We flip the current index with the index that element belongs to until the 
current index has its correct element. initial [3, 1, 5, 4, 2] -> [5, 1, 3, 4, 2] -> 
 -> [2, 1, 3, 4, 5] -> [1, 2, 3, 4, 5].

Example 2:
Input: [2, 6, 4, 3, 1, 5]
Output: [1, 2, 3, 4, 5, 6]

Example 3:
Input: [1, 5, 6, 4, 3, 2]
Output: [1, 2, 3, 4, 5, 6]
'''

def cyclicSort(nums):
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if i != j:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    return nums

nums = [3, 1, 5, 4, 2]
print(cyclicSort(nums))
nums2 = [2, 6, 4, 3, 1, 5]
print(cyclicSort(nums2))
nums3 = [1, 5, 6, 4, 3, 2]
print(cyclicSort(nums3))
