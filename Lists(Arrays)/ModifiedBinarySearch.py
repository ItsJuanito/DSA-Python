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