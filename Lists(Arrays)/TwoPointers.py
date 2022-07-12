'''
11. Container With Most Water

(Medium)

Problem Statement:
You are given an integer array height of length n. There are n vertical lines drawn such that the two 
endpoints of the ith line are (i, 0) and (i, height[i]). Find two lines that together with the x-axis 
form a container, such that the container contains the most water. Return the maximum amount of water a 
container can store.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1
'''

def maxArea(height):
    left = 0
    right = len(height) - 1
    max_water = 0
    # loop through the list
    while left < right:
        # store the minimum height of the two lines
        current_height = min(height[left], height[right])
        # calculate the width
        current_width = right - left
        # calculate the area
        current_water = current_height * current_width
        # get max area
        max_water = max(max_water, current_water)
        # move pointers
        if height[left] < height[right]:
            # move left pointer up one
            left += 1
        else:
            # move right mpointer down one
            right -= 1
    # return the maximum area
    return max_water

height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))
# Output: 49
height2 = [1, 1]
print(maxArea(height2))
# Output: 1

'''
Sorted Two Sum

(Easy)

Problem Statement:
Given a sorted array of integers nums and an integer target, return indices of the two numbers such that 
they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: True
Explanation: Because nums[0] + nums[1] == 9, we return True.

Example 2:
Input: nums = [3,2,4], target = 6
Output: True

Example 3:
Input: nums = [1,3], target = 6
Output: False
'''

def twoSum(nums, target):
    # initiate start and end variables
    left = 0
    right = len(nums) - 1
    # loop through the list while left is less than right
    while left < right:
        # calculate the sum
        sum = nums[left] + nums[right]
        # if the sum is equal to the target then 
        if sum == target:
            return True
        # else if the sum is less than the target, decrease left by 1
        elif sum < target:
            left += 1
        # else if the sum is greater than the target, increase right by 1
        else:
            right -= 1
    # return False if the target was never found
    return False

nums = [2,7,11,15]
target = 9
print(twoSum(nums, target))
# Output: True
nums2 = [3, 2, 4]
target2 = 6
print(twoSum(nums2, target2))
# Output: True
nums3 = [1, 3]
target3 = 6
print(twoSum(nums3, target3))
# Output: False


'''
Remove Duplicates

(easy)

Problem Statement 
Given an array of sorted numbers, remove all duplicates from it. You should not use any extra space; 
after removing the duplicates in-place return the new length of the array.

Example 1:
Input: [2, 3, 3, 3, 6, 9, 9]
Output: 4
Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].

Example 2:
Input: [2, 2, 2, 11]
Output: 2
Explanation: The first two elements after removing the duplicates will be [2, 11].
'''

def remove_Duplicates(nums):
    # initiate variables
    left = 0
    result = 0
    # loop through the array
    for right in range(1, len(nums)):
        # if the current number is the same as the previous number
        if nums[left] == nums[right]:
            # increment result
            result += 1
        # increment left
        left += 1
    # return result
    return result

print(remove_Duplicates([2, 3, 3, 3, 6, 9, 9]))
# Output: 3
print(remove_Duplicates([2, 2, 2, 11]))
# Output: 2


'''
Subarray of numbers less than given product

Problem Statement 

(medium)

Given an array with positive numbers and a target number, 
find all of its contiguous subarrays whose product is less than the target number.

Example 1:
Input: [2, 5, 3, 10], target=30 
Output: [2], [5], [2, 5], [3], [5, 3], [10]
Explanation: There are six contiguous subarrays whose product is less than the target.

Example 2:
Input: [8, 2, 6, 5], target=50 
Output: [8], [2], [8, 2], [6], [2, 6], [5], [6, 5] 
Explanation: There are seven contiguous subarrays whose product is less than the target.
'''

def find_subarrays(nums, target):
    result = []
    left = 0
    for right in range(1, len(nums)):
        if nums[left] < target:
                result.append([nums[right]])
        if nums[left] * nums[right] < target:
            result.append([nums[left], nums[right]])
        left += 1
    return result

print(find_subarrays([2, 5, 3, 10], 30))
print(find_subarrays([8, 2, 6, 5], 50))


# [2, 5, 3, 10]
# [2], [5], [3], [10]
# [2, 5], [5, 3]