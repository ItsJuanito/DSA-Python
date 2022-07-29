import sys
from BinaryTree import TreeNode

sys.path.append('..')
from Queue.Queue import Queue

a = TreeNode(10)
a.insert(4)
a.insert(6)
a.insert(12)

b = TreeNode(4)
b.insert(2)
b.insert(10)
b.insert(8)
b.insert(5)

'''
 Tree Structure (a):
          10
       /      \
      4       12
    /   \    /   \
  None   6 None  None

Tree Structure (b):
          4
      /      \
     2       10
    / \      / \
 None None 8   None
           /  \
          5   None
        /   \
     None   None
'''

def breathFirstSearch(root):
    if root == None:
        return []
    result = []
    queue = Queue()
    queue.enqueue(root)
    while queue.size() > 0:
        current = queue.dequeue()
        result.append(current.data)
        if current.left:
            queue.enqueue(current.left)
        if current.right:
            queue.enqueue(current.right)
    return result

print(breathFirstSearch(a))
# Output: [10, 4, 12, 6]
print(breathFirstSearch(b))
# Output: [4, 2, 10, 8, 5]

'''
Binary Tree Level Order Traversal

(medium)

Problem Statement: Given a binary tree, populate an array to represent its level-by-level traversal. 
You should populate the values of all nodes of each level from left to right in separate sub-arrays.

Example 1:
Input: [10, 4, 12, 6]
Output: [[10], [4, 12], [6]]

Example 2:
Input: [4, 2, 10, 8, 5]
Output: [[4], [2, 10], [8], [5]]
'''

def levelBFS(root):
    if root == None:
        return []
    result = []
    queue = Queue()
    queue.enqueue(root)
    while queue.size() > 0:
        level = []
        for _ in range(queue.size()):
            current = queue.dequeue()
            level.append(current.data)
            if current.left:
                queue.enqueue(current.left)
            if current.right:
                queue.enqueue(current.right)
        result.append(level)
    return result

print(levelBFS(a))
# Output: [[10], [4, 12], [6]]
print(levelBFS(b))
# Output: [[4], [2, 10], [8], [5]]