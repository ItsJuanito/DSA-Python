from functools import cache

'''
62. Unique Paths

(medium)

There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). 
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either 
down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach 
the bottom-right corner.

[s][.][.][.][.][.][.]
[.][.][.][.][.][.][.]
[.][.][.][.][.][.][f]

Example 1:
Input: m = 3, n = 7
Output: 28

Example 2:
Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
'''

def uniquePaths(m, n):
    # add cache to speed up previous moves
    @cache
    def dp(i, j):
        # if we are at the bottom right corner then return 1
        if i == m - 1 and j == n - 1:
            return 1
        # if we are out of bounds then return 0
        if i > m or j > n:
            return 0
        # return the sum of all ways
        return dp(i + 1, j) + dp(i, j + 1)
    # return the function starting at the top left corner
    return dp(0, 0)

print(uniquePaths(3, 7))
# Output: 28
print(uniquePaths(3, 2))
# Output: 3

'''
63. Unique Paths II

(medium)

You are given an m x n integer array grid. There is a robot initially located at the top-left 
corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). 
The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes 
cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

[s][0][0]
[0][1][0]
[0][0][f]

Example 1:
Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

Example 2:
Input: obstacleGrid = [[0,1],[0,0]]
Output: 1
'''

def uniquePathsWithObstacles(obstacleGrid):
    # add cache to speed up previous moves
    @cache
    def dp(i, j):
        # if we have reached an obsticale then return 0
        if obstacleGrid[i][j] == 1:
            return 0
        # if we have reached the bottom right corner then return 1
        if i == len(obstacleGrid) - 1 and j == len(obstacleGrid[0]) - 1:
            return 1
        # create path counter
        num_ways = 0
        # if down move is valid then go down
        if i + 1 < len(obstacleGrid):
            # add that path to num_ways
            num_ways += dp(i + 1, j)
        # if right move is valid then go right
        if j + 1 < len(obstacleGrid[0]):
            # add that path to num_ways
            num_ways += dp(i, j + 1)
        # return num_ways once finished
        return num_ways
    # return funciton
    return dp(0, 0)

obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
print(uniquePathsWithObstacles(obstacleGrid))
# Output: 2
obstacleGrid = [[0,1],[0,0]]
print(uniquePathsWithObstacles(obstacleGrid))
# Output: 1