import sys
import string
from BinaryTree import TreeNode

sys.path.append('..')
from Stack.Stack import Stack

a = TreeNode(5)
a.insert(2)
a.insert(1)
a.insert(8)
a.insert(6)

b = TreeNode(7)
b.insert(10)
b.insert(9)
b.insert(5)

c = TreeNode(5)
c.insert(3)
c.insert(7)
c.insert(4)

'''
Tree Structre (a):
                5
             /     \
            2       8
          /  \     /  \
         1  None  6  None
       /   \    /   \
     None None None None

Tree Strucutre (b):
                 7
             /       \
            5         10
          /   \     /   \
       None  None  9    None
                 /   \
               None  None

Tree Structure (c):
                5
             /     \
            2       7 
          /   \   /   \
        None   4 None None
'''

def depthFirstSearch(root):
    # if the root is None then return an empty list
    if root == None:
        return []
    # create a results list
    result = []
    # initiate a stack
    stack = Stack()
    # populate the stack witht the root
    stack.push(root)
    # while the stack is not empty
    while stack.size() > 0:
        # set the peak equal to the current node
        current = stack.pop()
        # append the current data to the results list
        result.append(current.data)
        # if current has a right child then add it to the stack
        if current.right:
            stack.push(current.right)
        # if current has a left child then add it to the stack
        if current.left:
            stack.push(current.left)
    # return the results list
    return result

print(depthFirstSearch(a))
# Output: [5, 2, 1, 8, 6]
print(depthFirstSearch(b))
# Output: [7, 5, 10, 9]

'''
Binary Tree Path Sum

(easy)

Problem Statement: Given a binary tree and a number ‘S’, find if the tree has a path from root-to-leaf 
such that the sum of all the node values of that path equals ‘S’.

Example 1:
Input: [5, 2, 1, 8, 6], sum = 8
Output: True

Example 2:
Input: [7, 5, 10, 9], sum = 23
Output: False
'''

def hasPath(root, sum):
    # if the root is None then return False
    if root is None:
        return False
    # if the root is equal to the sum and the root has no children then return True
    if root.data == sum and root.left is None and root.right is None:
        return True
    # return the recursive call with each child left or right with the sum subtracted by the data
    return hasPath(root.left, sum - root.data) or hasPath(root.right, sum - root.data)

print(hasPath(a, 8))
# Output: True
print(hasPath(a, 6))
# Output: False
print(hasPath(b, 12))
# Output: True
print(hasPath(b, 23))
# Output: False

'''
Count Paths for a Sum

(medium)

Problem Statement: Given a binary tree and a number ‘S’, find all paths in the tree such that the sum of all 
the node values of each path equals ‘S’. Please note that the paths can start or end at any node but all paths 
must follow direction from parent to child (top to bottom).

Example 1:
Input: [5, 2, 1, 8, 6], sum = 12
Output: 0

Example 2:
Input: [5, 2, 7, 4], sum = 12
Output: 2
'''

def count_paths(root, sum):
    # return the recursive call
    return find_current_count(root, sum, 0)

def find_current_count(root, sum, count):
    # if there is no root then return 0
    if root is None:
        return 0
    # if the current value is equal to the sum then incriment 1 to count
    if root.data == sum:
        count += 1
    # return the count + the recursive calls to get the final count
    return count + find_current_count(root.left, sum, count) + find_current_count(root.right, sum, count) + find_current_count(root.left, sum - root.data, count) + find_current_count(root.right, sum - root.data, count)

print(count_paths(a, 12))
# Output: 0
print(count_paths(c, 12))
# Output: 2

'''
257. Binary Tree Paths

(easy)

Given the root of a binary tree, return all root-to-leaf paths in any order.

Example 1:
Input: root = [5, 2, 1, 8, 6]
Output: ['5->2->1', '5->8->6']

Example 2:
Input: root = [7, 5, 10, 9]
Output: ['7->5', '7->10->9']
'''

def binaryTreePaths(root):
    result = []
    def dfs(root, string=""):
        if not root:
            return
        string += str(root.data)
        if (not root.left) and (not root.right):
            result.append(string)
        else:
            string += "->"
        dfs(root.left, string)
        dfs(root.right, string)
    dfs(root)
    return result

print(binaryTreePaths(a))
# Output: ['5->2->1', '5->8->6']
print(binaryTreePaths(b))
# Output: ['7->5', '7->10->9']


'''
988. Smallest String Starting From Leaf

(medium)

You are given the root of a binary tree where each node has a value in the range [0, 25] representing 
the letters 'a' to 'z'.

Return the lexicographically smallest string that starts at a leaf of this tree and ends at the root.

Example 1:
Input: root = [5, 2, 1, 8, 6]
Output: "bcf"

Example 2:
Input: root = [7, 5, 10, 9]
Output: "fh"
'''

def smallestFromLeaf(root):
    s = string.ascii_lowercase
    letters = dict()
    for idx, char in enumerate(s):
        letters[idx] = char
    result = []
    def dfs(root, string=""):
        if not root:
            return
        string += letters[root.data]
        if (not root.left) and (not root.right):
            result.append(string[::-1])
            return
        dfs(root.left, string)
        dfs(root.right, string)
    dfs(root)
    result = sorted(result)
    return result[0]

print(smallestFromLeaf(a))
# Output: 'bcf'
print(smallestFromLeaf(b))
# Output: 'fh'