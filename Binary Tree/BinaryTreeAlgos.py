import sys
from BinaryTree import TreeNode

sys.path.append('..')
from Queue.Queue import Queue

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
c.insert(8)

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
        None   4 None  8
'''


'''
199. Binary Tree Right Side View

(medium)

Given the root of a binary tree, imagine yourself standing on the right side of it, 
return the values of the nodes you can see ordered from top to bottom.

Example 1:
Input: root = [5, 2, 8, 1, 6]
Output: [5, 8, 6]

Example 2:
Input: root = [7, 5, 10, 9]
Output: [7, 10, 9]
'''

def rightSideView(root):
    if not root:
        return
    queue = Queue()
    queue.enqueue(root)
    nodes = dict()
    level = 0
    while queue.size() > 0:
        level += 1
        size = queue.size()
        temp = []
        for _ in range(size):
            current = queue.dequeue()
            temp.append(current.data)
            if current.left:
                queue.enqueue(current.left)
            if current.right:
                queue.enqueue(current.right)
        nodes[level] = temp
    result = []
    for key in nodes:
        result.append(nodes[key][-1])
    return result

print(rightSideView(a))
# Output: [5, 8 , 6]
print(rightSideView(b))
# Output: [7, 10, 9]

'''
2583. Kth Largest Sum in a Binary Tree

(medium)

You are given the root of a binary tree and a positive integer k.

The level sum in the tree is the sum of the values of the nodes that are on the same level.

Return the kth largest level sum in the tree (not necessarily distinct). If there are fewer 
than k levels in the tree, return -1.

Note that two nodes are on the same level if they have the same distance from the root.

Example 1:
Input: root = [5, 2, 8, 1, 6], k = 2
Output: 7

Example 2:
Input: root = [7, 5, 10, 9], k = 1
Output: 15
'''

def kthLargestLevelSum(root, k):
    if not root:
        return 0
    queue = Queue()
    queue.enqueue(root)
    level = 0
    result = []
    while queue.size() > 0:
        sum_ = 0
        level += 1
        size = queue.size()
        for _ in range(size):
            current = queue.dequeue()
            sum_ += current.data
            if current.left:
                queue.enqueue(current.left)
            if current.right:
                queue.enqueue(current.right)
        result.append(sum_)
    result = sorted(result)
    return result[-k] if k <= len(result) else -1

print(kthLargestLevelSum(a, 2))
# Output: 7
print(kthLargestLevelSum(b, 1))
# Output: 15

'''
1161. Maximum Level Sum of a Binary Tree

(medium)

Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

Example 1:
Input: root = [5, 2, 8, 1, 6]
Output: 2

Example 2:
Input: root = [5, 2, 7, 4, 8]
Output: 3
'''

def maxLevelSum(root):
    if not root:
        return 0
    queue = Queue()
    queue.enqueue(root)
    level_sums = dict()
    level = 0
    while queue.size() > 0:
        sum_ = 0
        level += 1
        size = queue.size()
        for _ in range(size):
            current = queue.dequeue()
            sum_ += current.data
            if current.left:
                queue.enqueue(current.left)
            if current.right:
                queue.enqueue(current.right)
        level_sums[level] = sum_
    result = max(level_sums, key=level_sums.get)
    return result

print(maxLevelSum(a))
# Output: 2
print(maxLevelSum(c))
# Output: 3