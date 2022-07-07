'''
1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold

(Medium)

Problem Statement:
Given an array of integers arr and two integers k and threshold, return the number of sub-arrays of size k and average greater than or equal to threshold.

Example 1:
Input: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
Output: 3
Explanation: Sub-arrays [2,5,5],[5,5,5] and [5,5,8] have averages 4, 5 and 6 respectively. All other sub-arrays of size 3 have averages less than 4 (the threshold).

Example 2:
Input: arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5
Output: 6
Explanation: The first 6 sub-arrays of size 3 have averages greater than 5. Note that averages are not integers.
'''

def numOfSubarrays(arr, k, threshold):
    # initiate variables
    sum = 0
    update = 0
    count = 0
    # loop through the arr
    for window in range(len(arr)):
        # update the sum
        sum += arr[window]
        # check to see if iterator is greater than k - 1
        if window >= k - 1:
            # get calculate the average
            average = sum // k
            # subtract from sum (sliding window)
            sum -= arr[update] 
            # increment update
            update += 1
            # check if average is >= threshold
            if average >= threshold:
                # increment count
                count += 1
    # return count
    return count
    
arr = [2,2,2,2,5,5,5,8]
k = 3
threshold = 4
print(str(numOfSubarrays(arr, k, threshold)))
# Output: 3
arr2 = [11,13,17,23,29,31,7,5,2,3]
k2 = 3
threshold2 = 5
print(str(numOfSubarrays(arr2, k2, threshold2)))
# Output : 6

'''
Number of Sub-arrays of Size K with Greatest Sum.

(Easy)

Problem Statement:
Given an array of positive numbers and a positive number k, find the maximum sum of any contiguous subarray of size k.

Example 1:
Input: [2, 1, 5, 1, 3, 2], k=3 
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].

Example 2:
Input: [2, 3, 4, 1, 5], k=2 
Output: 7
Explanation: Subarray with maximum sum is [3, 4].
'''

def max_sub_array_of_size_k(arr, k):
    # initiate variables
    window_sum = 0
    max_sum = 0
    update = 0
    # loop through the array
    for window in range(len(arr)):
        # add item to sum
        window_sum += arr[window]
        # check if iterator is >= k - 1
        if window >= k - 1:
            # update max_sum and compare sums
            max_sum = max(max_sum, window_sum)
            # subtract from sum (sliding window)
            window_sum -= arr[update]
            # increment update
            update += 1
    # return max_sum
    return max_sum

arr = [2, 1, 5, 1, 3, 2]
k = 3 
print(str(max_sub_array_of_size_k(arr, k)))
# Output: 9
arr2 = [2, 3, 4, 1, 5]
k2 = 2
print(str(max_sub_array_of_size_k(arr2, k2)))
# Output: 7

'''
Smallest Subarray with Given Sum.

(Medium)

Problem Statement:
Given an array of n size. Find the smallest subarray that is greater than or equal to the target.

Example 1:
Input: [3, 1, 5, 1, 4, 7], target=6 
Output: 2
Explanation: Subarray with smallest size is [1, 5] or [5, 1].

Example 2:
Input: [2, 6, 1, 4, 5, 7], target=5 
Output: 1
Explanation: Subarray with smallest size is [5].
'''

def smallest_sum_sub_array(arr, target):
    # initiate variables
    window_start = 0
    window_sum = 0
    # large value
    size = 100000
    # loop through the array 
    for window in range(len(arr)):
        # add the current item to the sum
        window_sum += arr[window]
        # while the current sum is >= target
        while window_sum >= target:
            # get min size of the subarray
            size = min(size, window - window_start + 1)
            # subtract the first item to slide window
            window_sum -= arr[window_start]
            # increment window start
            window_start += 1
    # return the smallest size
    return size

nums = [3, 1, 5, 1, 4, 7]
target = 6
nums2 = [2, 6, 1, 4, 5, 7]
target2 = 5
print(smallest_sum_sub_array(nums, target))
# Output: 2
print(smallest_sum_sub_array(nums2, target2))
# Output: 1
