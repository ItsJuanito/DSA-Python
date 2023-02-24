'''
463. Island Perimeter

(easy)

Problem Statement: You are given row x col grid representing a map where grid[i][j] = 1 represents land 
and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely 
surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. 
One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. 
Determine the perimeter of the island.


[0][1][0][0]
[1][1][1][0]
[0][1][0][0]
[1][1][0][0]

Example 1:
Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16
Explanation: The perimeter is the 16 since each side represents 1 point and there are 4 points per island. 
If the neighbor of that island is 1 then subtract 1 point from your perimeter. For example, index (0, 1) has
1 island neighbor which is index (1, 1) and the rest of the sides are occupied by water(0's) and out of bounds 
so its perimeter is 4 - 1.

Example 2:
Input: grid = [[1]]
Output: 4

Example 3:
Input: grid = [[1,0]]
Output: 4
'''

# helper function
def isValid(n, m, i, j):
    #check if the coordinates are in the matrix
    return (0 <= i and i < n) and (0 <= j and j < m) 

# helper function
def checkNeighbors(grid, n, m, i, j):
    # coordinates: left, up, right, down
    x = [-1, 0, 1, 0]
    y = [0, -1, 0, 1]
    # set perimeter to 4 initially
    p = 4
    # loop through all posible neihgbors
    for k in range(len(x)):
        # if there is a neighbor
        if isValid(n, m, i + x[k], j + y[k]):
            # if the neighbor is a 1 then subtract 1 from the perimeter
            if grid[i + x[k]][j + y[k]] == 1:
                p -= 1
    return p

def islandPerimeter(grid):
    # store bounds
    n = len(grid)
    m = len(grid[0])
    # perimeter will be zero at first
    perimeter = 0
    # loop through each point in the grid
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                # add the island's perimeter to the overall perimeter
                perimeter += checkNeighbors(grid, n, m, i, j)
    return perimeter

if __name__ == "__main__":
    grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
    # Output: 16
    print(islandPerimeter(grid))
    grid = [[1]]
    # Output: 4
    print(islandPerimeter(grid))
    grid = [[1,0]]
    # Output: 4
    print(islandPerimeter(grid))

'''
link to another matrix problem: https://leetcode.com/problems/toeplitz-matrix/
'''