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

'''
Find Level Averages

(easy)

Problem Statement: Given a binary tree, populate an array to represent the averages of all of its levels.

Example 1:
Input: [10, 4, 12, 6]
Output: [10.0, 8.0, 6.0]

Example 2:
Input: [4, 2, 10, 8, 5]
Output: [4.0, 6.0, 8.0, 5.0]
'''

def find_level_averages(root):
    # initiate result list
    result = []
    # if root is none then return an empty list
    if root is None:
        return result
    # initiate queue
    queue = Queue()
    # populate queue with the root
    queue.enqueue(root)
    # while the queue is not empty
    while queue.size() > 0:
        # initiate data_Sum variable
        data_sum = 0
        # store the length of the queue
        length = queue.size()
        # loop through the length of the queue
        for _ in range(length):
            # set current equal to the peak
            current = queue.dequeue()
            # add the current data to the data_Sum variable
            data_sum += current.data
            # if there is a left child
            if current.left:
                # add the left child to the queue
                queue.enqueue(current.left)
            # if there is a right child
            if current.right:
                # add the right child to the queue
                queue.enqueue(current.right)
        # add the average of the level sum to the result list
        result.append(data_sum/length)
    # return the result
    return result

print(find_level_averages(a))
# Output: [10.0, 8.0, 6.0]
print(find_level_averages(b))
# Output: [4.0, 6.0, 8.0, 5.0]

'''
1302. Deepest Leaves Sum

(medium)

Problem Statement: Given the root of a binary tree, return the sum of values of its deepest leaves.

Example 1:
Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15

Example 2:
Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 19
'''

def deepestLeavesSum(root):
    if not root:
        return 0
    queue = Queue()
    queue.enqueue(root)
    depth = dict()
    d = 1
    while queue.size() > 0:
        size = queue.size()
        depth[d] = []
        for _ in range(size):
            current = queue.dequeue()
            depth[d].append(current.data)
            if current.left:
                queue.enqueue(current.left)
            if current.right:
                queue.enqueue(current.right)
        d += 1
    max_depth = len(depth)
    return sum(depth[max_depth])
print(deepestLeavesSum(a))
print(deepestLeavesSum(b))