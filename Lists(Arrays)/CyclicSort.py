'''
Cyclic Sort

(easy)

Problem Statement: We are given an array containing ‘n’ objects. Each object, when created, 
was assigned a unique number from 1 to ‘n’ based on their creation sequence. This means that 
the object with sequence number ‘3’ was created just before the object with sequence number ‘4’. 
Write a function to sort the objects in-place on their creation sequence number in O(n) and 
without any extra space. For simplicity, let’s assume we are passed an integer array containing 
only the sequence numbers, though each number is actually an object.

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
    # initiate interator
    i = 0
    # while i is less than the size of the array
    while i < len(nums):
        # set j equal to the index we are looking for
        j = nums[i] - 1
        # if i is not equal to that index
        if i != j:
            # swap both indexes
            nums[i], nums[j] = nums[j], nums[i]
        else:
            # otherwise increment i
            i += 1
    # return the array once done
    return nums

nums = [3, 1, 5, 4, 2]
print(cyclicSort(nums))
# Output: [1, 2, 3, 4, 5]
nums2 = [2, 6, 4, 3, 1, 5]
print(cyclicSort(nums2))
# Output: [1, 2 ,3, 4, 5, 6]
nums3 = [1, 5, 6, 4, 3, 2]
print(cyclicSort(nums3))
# Output: [1, 2, 3, 4, 5 ,6]

'''
Find All Duplicates

(Medium)

Problem Statement: We are given an unsorted array containing ‘n’ numbers taken from the range 1 to ‘n’. 
The array has some duplicates, find all the duplicate numbers without using any extra space.

Example 1:
Input: [3, 4, 4, 5, 5]
Output: [4, 5]

Example 2:
Input: [5, 4, 7, 2, 3, 5, 3]
Output: [3, 5]
'''

def find_all_duplicates(nums):
    # initiate iterator
    i = 0
    # loop through the list while i is less than the length of the list
    while i < len(nums):
        # set j equal to the the current element - 1
        j = nums[i] - 1
        # if the current element is not equal to the element at index j
        if nums[i] != nums[j]:
            # swap the two elements
            nums[i], nums[j] = nums[j], nums[i]
        else:
            # otherwise just increment i by 1
            i += 1
    # create a duplicates list
    duplicates = []
    # loop through the list again
    for i in range(len(nums)):
        # if the current element is not equal to the current index + 1
        if nums[i] != i + 1:
            # add the element to the duplicates list
            duplicates.append(nums[i])
    # return the duplicates list
    return duplicates

nums = [3, 4, 4, 5, 5]
print(find_all_duplicates(nums))
# Output: [4, 5]
nums2 = [5, 4, 7, 2, 3, 5, 3]
print(find_all_duplicates(nums2))
# Output: [3, 5]
