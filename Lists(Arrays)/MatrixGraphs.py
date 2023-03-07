import copy
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
766. Toeplitz Matrix

(easy)

Problem Statement: Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.

A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.

[1][2][3][4]
[5][1][2][3]
[6][5][1][2]

Example 1:
Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
Output: true
Explanation:
In the above grid, the diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.
Example 2:


Input: matrix = [[1,2],[2,2]]
Output: false
Explanation:
The diagonal "[1, 2]" has different elements.
'''

def isToeplitzMatrix(matrix):
    # store m and x sizes
    n = len(matrix)
    m = len(matrix[0])
    # loop through the bottom half of the matrix
    for i in range(n):
        # set row to i
        row = i
        # set column to 0
        col = 0
        # set first value to the initial value
        init = matrix[row][col]
        # loop through the matrix diagnally
        while row < n and col < m:
            # if the current number does not match the initial value then return false
            if matrix[row][col] != init:
                return False
            # update diagnal coordinates
            row += 1
            col += 1
    # loop through the top half of the matrix
    for i in range(m):
        # set row to 0 now
        row = 0
        # set col to i
        col = i
        # store the initial value
        init = matrix[row][col]
        # loop through the matrix diagnally
        while row < n and col < m:
            # if the current number does not match the initial value then return false
            if matrix[row][col] != init:
                return False
            # update diagnal coordinates
            row += 1
            col += 1
    return True

matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
print(isToeplitzMatrix(matrix))
# Output: False
matrix = [[1,2],[2,2]]
print(isToeplitzMatrix(matrix))
# Output: True

'''
2120. Execution of All Suffix Instructions Staying in a Grid

(medium)

There is an n x n grid, with the top-left cell at (0, 0) and the bottom-right cell at (n - 1, n - 1). 
You are given the integer n and an integer array startPos where startPos = [startrow, startcol] indicates 
that a robot is initially at cell (startrow, startcol).

You are also given a 0-indexed string s of length m where s[i] is the ith instruction for the robot: 
'L' (move left), 'R' (move right), 'U' (move up), and 'D' (move down).

The robot can begin executing from any ith instruction in s. It executes the instructions one by one towards 
the end of s but it stops if either of these conditions is met:

The next instruction will move the robot off the grid.
There are no more instructions left to execute.
Return an array answer of length m where answer[i] is the number of 
instructions the robot can execute if the robot begins executing from the ith instruction in s.

Example 1:
Input: n = 3, startPos = [0,1], s = "RRDDLU"
Output: [1,5,4,3,1,0]
Explanation: Starting from startPos and beginning execution from the ith instruction:
- 0th: "RRDDLU". Only one instruction "R" can be executed before it moves off the grid.
- 1st:  "RDDLU". All five instructions can be executed while it stays in the grid and ends at (1, 1).
- 2nd:   "DDLU". All four instructions can be executed while it stays in the grid and ends at (1, 0).
- 3rd:    "DLU". All three instructions can be executed while it stays in the grid and ends at (0, 0).
- 4th:     "LU". Only one instruction "L" can be executed before it moves off the grid.
- 5th:      "U". If moving up, it would move off the grid.

Example 2:
Input: n = 2, startPos = [1,1], s = "LURD"
Output: [4,1,0,0]
Explanation:
- 0th: "LURD".
- 1st:  "URD".
- 2nd:   "RD".
- 3rd:    "D".

Example 3:
Input: n = 1, startPos = [0,0], s = "LRUD"
Output: [0,0,0,0]
Explanation: No matter which instruction the robot begins execution from, it would move off the grid.
'''

# create a dictionary that stores all possible moves
moves = {
    'U' : [-1, 0], 
    'R' : [0, 1], 
    'D' : [1, 0], 
    'L' : [0, -1]
    }
# create an isValid function to check if the your location is within the bounds of n
def isValid(curr, next, n):
    x = curr[0] + next[0]
    y = curr[1] + next[1]
    return x < n and y < n and x >= 0 and y >= 0

def executeInstructions(n, startPos, s):
    # store count of valid moves
    result = []
    # loop through each move in s
    for i in range(len(s)):
        # create a counter variable
        count = 0
        # set initial position to the current position
        curr_pos = startPos
        # loop through the remaining valid moves
        for j in range(i, len(s)):
            # if the move is valid then update count, and current position
            if isValid(curr_pos, moves[s[j]], n):
                new_pos = moves[s[j]]
                curr_pos = [(curr_pos[0] + new_pos[0]), (curr_pos[1] + new_pos[1])]
                count += 1
            else:
                # if the move isn't valid then break and move to the next move
                break
        # add count to result
        result.append(count)
    # return the result list
    return result

n = 3
startPos = [0,1]
s = "RRDDLU"
print(executeInstructions(n, startPos, s))
# Output: [1,5,4,3,1,0]
n = 2
startPos = [1,1]
s = "LURD"
print(executeInstructions(n, startPos, s))
# Output: [4,1,0,0]
n = 1
startPos = [0,0]
s = "LRUD"
print(executeInstructions(n, startPos, s))
# Output: [0,0,0,0]

'''
73. Set Matrix Zeroes

(medium)

Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
'''
# create a transform function that takes the coordinates and the matrix
def transform(i, j, matrix):
    # loop through each row
    for x in range(len(matrix)):
        # set flag to False
        flag = False
        # if the x is the same as the i then set flag tp True
        if x == i:
            flag = True
        # loop through each column
        for y in range(len(matrix[x])):
            # if x is equal to i then set the value to 0
            if flag:
                matrix[x][y] = 0
            # if y is equal to j then set the value to 0
            if y == j:
                matrix[x][y] = 0

def setZeroes(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """
    # set m and n values
    m = len(matrix)
    n = len(matrix[0])
    # create a deep copy of the matrix to edit the original matrix
    grid = copy.deepcopy(matrix)
    # loop through each column
    for i in range(m):
        # loop through each column
        for j in range(n):
            # if the current value is a 0 then transform the matrix
            if grid[i][j] == 0:
                transform(i, j, matrix)
    # return the matrix
    return matrix

matrix = [[1,1,1],[1,0,1],[1,1,1]]
print(setZeroes(matrix))
# Output: [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
print(setZeroes(matrix))
# Output: [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]