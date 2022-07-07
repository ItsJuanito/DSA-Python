'''
11. Container With Most Water

(Medium)

Problem Statement:
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.

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