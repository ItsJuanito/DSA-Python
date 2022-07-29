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
    # if the root is none then return an empty list
    if root == None:
        return []
    # create a results array
    result = []
    # create a queue
    queue = Queue()
    # add the root to the queue
    queue.enqueue(root)
    # while the queue is not empty
    while queue.size() > 0:
        # make the current node the peek
        current = queue.dequeue()
        # add the data of the current node to the result
        result.append(current.data)
        # if there is a left node
        if current.left:
            # add the left node to the queue
            queue.enqueue(current.left)
        # if there is a right node
        if current.right:
            # add the right node to the queue
            queue.enqueue(current.right)
    # return the result
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
    # if the root is none
    if root == None:
        # return an empty list
        return []
    # create an results array
    result = []
    # create a queue
    queue = Queue()
    # add the root to the queue
    queue.enqueue(root)
    # while the queue is not empty
    while queue.size() > 0:
        # create a level array
        level = []
        # iterate through the size of the queue
        for _ in range(queue.size()):
            # set the peek to the current value
            current = queue.dequeue()
            # add the data of the current value to the level array
            level.append(current.data)
            # if there is a left child
            if current.left:
                # add the left child to the queue
                queue.enqueue(current.left)
            # if there is a right child
            if current.right:
                # add the right child to the queue
                queue.enqueue(current.right)
        # add the level array to the result array
        result.append(level)
    # return the result array
    return result

print(levelBFS(a))
# Output: [[10], [4, 12], [6]]
print(levelBFS(b))
# Output: [[4], [2, 10], [8], [5]]