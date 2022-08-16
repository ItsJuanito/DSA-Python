'''
Find All Subsets of a Set

(easy)

Problem Statement: Given a set with distinct elements, find all of its distinct subsets.

Example 1:
Input: [1, 3]
Output: [], [1], [3], [1,3]

Example 2:
Input: [1, 5, 3]
Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3]
'''

def find_subsets(nums):
    # create a subsets list
    subsets = []
    # append an empty set to the list
    subsets.append([])
    # loop through each element in nums
    for n in nums:
        # loop through each element in subset
        for i in range(len(subsets)):
            # copy the ith element and store it in temp list
            temp = subsets[i].copy()
            # append the current element to the temp list
            temp.append(n)
            # add the temp list to the subset
            subsets.append(temp)
    # return the subset
    return subsets

nums = [1, 3]
print(find_subsets(nums))
# Output: [[], [1], [3], [1, 3]]
nums2 = [1, 5, 3]
print(find_subsets(nums2))
# Output: [[], [1], [5], [1, 5], [3], [1, 3], [5, 3], [1, 5, 3]]


def find_subsets_with_duplicate(nums):
    nums.sort()
    subsets = []
    subsets.append([])
    start, end = 0, 0
    for i in range(len(nums)):
        start = 0
        if i > 0 and nums[i] == nums[i - 1]:
            start = end
        end = len(subsets)
        for j in range(start, end):
            temp = subsets[j].copy()
            temp.append(nums[i])
            subsets.append(temp)
    return subsets

nums = [1, 3, 3]
print(find_subsets_with_duplicate(nums))
nums2 = [1, 5, 3, 3]
print(find_subsets_with_duplicate(nums2))