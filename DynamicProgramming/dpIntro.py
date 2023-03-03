from functools import cache


'''
397. Integer Replacement

(medium)

Given a positive integer n, you can apply one of the following operations:

If n is even, replace n with n / 2.
If n is odd, replace n with either n + 1 or n - 1.
Return the minimum number of operations needed for n to become 1.

Example 1:
Input: n = 8
Output: 3
Explanation: 8 -> 4 -> 2 -> 1

Example 2:
Input: n = 7
Output: 4
Explanation: 7 -> 8 -> 4 -> 2 -> 1
or 7 -> 6 -> 3 -> 2 -> 1

Example 3:
Input: n = 4
Output: 2
'''

def integerReplacement(n):
    # create a result list to store all the number of operations
    result = []
    # add cache to store previous iterations
    @cache
    # create a dp function that passes the number and its operations
    def dp(num, turns=0):
        # if the number is one then we have reached the end
        if num == 1:
            # add the number of operations to the result array
            result.append(turns)
            return
        # if the number is even then call dp and divide the num buy 2
        if num % 2 == 0:
            dp(num//2, turns + 1)
        # otherwise call dp and go through two different paths where the number
        # is even but greater by one and another that is less than one
        else:
            dp(num + 1, turns + 1)
            dp(num - 1, turns + 1)
    # call the dp function
    dp(n)
    # return the minimum operation in result
    return min(result)

print(integerReplacement(8))
# Output: 3
print(integerReplacement(7))
# Output: 4
print(integerReplacement(4))
# Output: 2


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

'''
64. Minimum Path Sum

(medium)

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, 
which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example 1:
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

Example 2:
Input: grid = [[1,2,3],[4,5,6]]
Output: 12
'''

def minPathSum(grid):
    # add cache to speed up previous moves
    @cache
    # create s dp function that passes i and j coordinates
    def dp(i, j):
        # if we have reached the bottom right corner(the end) then return the value
        if i == len(grid) - 1 and j == len(grid[0]) - 1:
            return grid[i][j]
        # create a result list to store the sums
        result = []
        # if the bottom move is valid then add the value to result and the other posible moves
        if i + 1 < len(grid):
            result.append(grid[i][j] + dp(i + 1, j))
        # if the right move is valid then add the value to result and the other posible moves
        if j + 1 < len(grid[0]):
            result.append(grid[i][j] + dp(i, j + 1))
        # lastly return the smallest sum value
        return min(result)
    # return the function call starting at 0, 0 (top, left)
    return dp(0, 0)

grid = [[1,3,1],[1,5,1],[4,2,1]]
print(minPathSum(grid))
# Output: 7 
grid = [[1,2,3],[4,5,6]]
print(minPathSum(grid))
# Output: 12