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
    # return if there is no root
    if not root:
        return
    # initiate queue and populate it with the root
    queue = Queue()
    queue.enqueue(root)
    # create a dictionary to hold every node of each level
    nodes = dict()
    level = 0
    # while the queue is populated
    while queue.size() > 0:
        # update the current level
        level += 1
        # store the size of the queue
        size = queue.size()
        # create a temperary list to store each node value
        temp = []
        # loop through the level
        for _ in range(size):
            # pop the node
            current = queue.dequeue()
            # add the value of that node to temp
            temp.append(current.data)
            # if the node has a left child then add it to the queue
            if current.left:
                queue.enqueue(current.left)
            # if the node has a right child then add it to the queue
            if current.right:
                queue.enqueue(current.right)
        # add temp to its corresponding level
        nodes[level] = temp
    # create a result list to store the node visiible from the right
    result = []
    # loop through each leve
    for key in nodes:
        # add the right most visible value to result
        result.append(nodes[key][-1])
    # return result
    return result

print(rightSideView(a))
# Output: [5, 8, 6]
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
    # if there is not a root then return 0
    if not root:
        return 0
    # initiate queue and add the root
    queue = Queue()
    queue.enqueue(root)
    # initiate level as 0
    level = 0
    # create a result list
    result = []
    # while the queue is populated
    while queue.size() > 0:
        # reset sum
        sum_ = 0
        # increment level by 1
        level += 1
        # store size of the queue
        size = queue.size()
        # loop through the leve
        for _ in range(size):
            # pop the node form the queue
            current = queue.dequeue()
            # add current value to the sum
            sum_ += current.data
            # if the node has a left child then add it to the queue
            if current.left:
                queue.enqueue(current.left)
            # if the node has a right child then add it to the queue
            if current.right:
                queue.enqueue(current.right)
        # add the sum to result
        result.append(sum_)
    # sort the list once done
    result = sorted(result)
    # return the last k value if there is a k otherwise return -1
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
    # if there is no root then return 0
    if not root:
        return 0
    # initiate the queue and populate it with the root
    queue = Queue()
    queue.enqueue(root)
    # create dictionary to store levels and their sums
    level_sums = dict()
    level = 0
    # while the queue is not empty
    while queue.size() > 0:
        # set current sum to 0
        sum_ = 0
        # increment the sum
        level += 1
        # store the size of the queue
        size = queue.size()
        # loop through the level
        for _ in range(size):
            # pop the node from the queue
            current = queue.dequeue()
            # add the node's value to the sum
            sum_ += current.data
            # if the node has a left child then add it to the queue
            if current.left:
                queue.enqueue(current.left)
            # if the node has a right child then add it to the queue
            if current.right:
                queue.enqueue(current.right)
        # add the corresponding sum to the level
        level_sums[level] = sum_
    # get the key(level) with max value(sum) of the tree
    result = max(level_sums, key=level_sums.get)
    # return the level with the max sum
    return result

print(maxLevelSum(a))
# Output: 2
print(maxLevelSum(c))
# Output: 3

'''
129. Sum Root to Leaf Numbers

(medium)

You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
Return the total sum of all root-to-leaf numbers. Test cases are generated so 
that the answer will fit in a 32-bit integer.

A leaf node is a node with no children.

Example 1:
Input: root = [1,2,3]
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
'''

def sumNumbers(root):
    nums = []
    def dfs(root, string=""):
        if not root:
            return
        string += str(root.data)
        if (root.left is None) and (root.right is None):
            nums.append(string)
            string=""
            return
        dfs(root.left, string)
        dfs(root.right, string)
    dfs(root)
    nums = [int(num) for num in nums]
    return sum(nums)

print(sumNumbers(a))
# Output: 1107