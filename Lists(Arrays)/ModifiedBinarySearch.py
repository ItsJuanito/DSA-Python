'''
Find Max in Bitonic Array

(easy)

Problem Statement: 
Find the maximum value in a given Bitonic array. An array is considered bitonic if it is 
monotonically increasing and then monotonically decreasing. Monotonically increasing or 
decreasing means that for any index i in the array arr[i] != arr[i+1].

Example 1:
Input: [1, 3, 8, 12, 4, 2]
Output: 12
Explanation: The maximum number in the input bitonic array is '12'.

Example 2:
Input: [3, 8, 3, 1]
Output: 8

Example 3:
Input: [1, 3, 8, 12]
Output: 12

Example 4:
Input: [10, 9, 8]
Output: 10
'''

def find_max_in_bitonic_array(nums):
    # set start and end values
    start, end = 0, len(nums) - 1
    # whiel start is less than end
    while start <= end:
        # initiate mid value
        mid = (start + end) // 2
        # if the mid is equal to the last index
        if mid == len(nums) - 1:
            # return the value at that index
            return nums[mid]
        # if the mid is less than the last index and the current value is less than the next value
        if mid < len(nums) - 1 and nums[mid] < nums[mid + 1]:
            # increase start to the new position
            start = mid + 1
        else:
            # if mid - 1 is positive and the current value is greater than the previous value
            if mid - 1 >= 0 and nums[mid] > nums[mid - 1]:
                # return the current value
                return nums[mid]
            # else if mid is equal to 0
            elif mid == 0:
                # return the current value
                return nums[mid]
            else:
                # decrease end to the new current position
                end = mid - 1

nums = [1, 3, 8, 12, 4, 2]
print(find_max_in_bitonic_array(nums))
# Output: 12
nums2 = [3, 8, 3, 1]
print(find_max_in_bitonic_array(nums2))
# Output: 8

'''
Orderd-Agnostic Binary Search

(easy)

Problem Statement: 
Given a sorted array of numbers, find if a given number ‘key’ is present in the array. 
Though we know that the array is sorted, we don’t know if it’s sorted in ascending or 
descending order. You should assume that the array can have duplicates. Write a function 
to return the index of the ‘key’ if it is present in the array, otherwise return -1.

Example 1:
Input: [4, 6, 10], key = 10
Output: 2

Example 2:
Input: [1, 2, 3, 4, 5, 6, 7], key = 5
Output: 4

Example 3:
Input: [10, 6, 4], key = 10
Output: 0

Example 4:
Input: [10, 6, 4], key = 4
Output: 2
'''

def binarySearch(arr, target):
    # check to see if the first element is the only element
    if arr[0] == arr[-1]:
        return 0
    # if the array is in ascending order
    if arr[0] < arr[-1]:
        # set start to the first index
        start = 0
        # set end to the last index
        end = len(arr) - 1
        # while start is less than or equal to end
        while start <= end:
            # mid becomes the current index
            mid = (start + end) // 2
            # if the current index is smaller than the target
            if arr[mid] < target:
                # set start to mid + 1
                start = mid + 1
            # else if the current index is bigger than the target
            elif arr[mid] > target:
                # set end to mid - 1
                end = mid - 1
            else:
                # otherwise return mid
                return mid
    # if the array is in descending order
    if arr[0] > arr[-1]:
        # set start to the first index
        start = 0
        # set end to the last index
        end = len(arr) - 1
        # while start is less than or equal to end
        while start <= end:
            mid = (start + end) // 2
            # if the current index is bigger than the target
            if arr[mid] > target:
                # set start to mid + 1
                start = mid + 1
            # else if the current index is smaller than the target
            elif arr[mid] < target:
                # set end to mid - 1
                end = mid - 1
            else:
                # otherwise return mid
                return mid
    # return -1 if there is no output to produce
    return -1

nums = [4, 6, 10]
target = 10
print(binarySearch(nums, target))
# Output: 2
nums2 = [1, 2, 3, 4, 5, 6, 7]
target2 = 5
print(binarySearch(nums2, target2))
# Ouput: 4
    