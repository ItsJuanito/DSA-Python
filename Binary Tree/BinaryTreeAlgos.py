'''
199. Binary Tree Right Side View
Medium
9.5K
573
Companies
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

 

Example 1:


Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
Example 2:

Input: root = [1,null,3]
Output: [1,3]
Example 3:

Input: root = []
Output: []
'''

def rightSideView(root):
    if not root:
        return
    queue = [root]
    nodes = dict()
    level = 0
    while queue:
        level += 1
        size = len(queue)
        temp = []
        for _ in range(size):
            current = queue.pop()
            temp.append(current.val)
            if current.left:
                queue.insert(0, current.left)
            if current.right:
                queue.insert(0, current.right)
        nodes[level] = temp
    result = []
    for key in nodes:
        result.append(nodes[key][-1])
    return result

'''
2583. Kth Largest Sum in a Binary Tree
Medium
104
3
Companies
You are given the root of a binary tree and a positive integer k.

The level sum in the tree is the sum of the values of the nodes that are on the same level.

Return the kth largest level sum in the tree (not necessarily distinct). If there are fewer than k levels in the tree, return -1.

Note that two nodes are on the same level if they have the same distance from the root.

 

Example 1:


Input: root = [5,8,9,2,1,3,7,4,6], k = 2
Output: 13
Explanation: The level sums are the following:
- Level 1: 5.
- Level 2: 8 + 9 = 17.
- Level 3: 2 + 1 + 3 + 7 = 13.
- Level 4: 4 + 6 = 10.
The 2nd largest level sum is 13.
Example 2:


Input: root = [1,2,null,3], k = 1
Output: 3
Explanation: The largest level sum is 3.
'''

def kthLargestLevelSum(root, k):
    if not root:
        return 0
    queue = [root]
    level = 0
    result = []
    while queue:
        sum_ = 0
        level += 1
        size = len(queue)
        for _ in range(size):
            current = queue.pop()
            sum_ += current.val
            if current.left:
                queue.insert(0, current.left)
            if current.right:
                queue.insert(0, current.right)
        result.append(sum_)
    result = sorted(result)
    return result[-k] if k <= len(result) else -1

'''
1161. Maximum Level Sum of a Binary Tree
Medium
1.8K
65
Companies
Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

 

Example 1:


Input: root = [1,7,0,7,-8,null,null]
Output: 2
Explanation: 
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.
Example 2:

Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
Output: 2
'''

def maxLevelSum(root):
    if not root:
        return 0
    queue = [root]
    level_sums = dict()
    level = 0
    while queue:
        sum_ = 0
        level += 1
        size = len(queue)
        for _ in range(size):
            current = queue.pop()
            sum_ += current.val
            if current.left:
                queue.insert(0, current.left)
            if current.right:
                queue.insert(0, current.right)
        level_sums[level] = sum_
    result = max(level_sums, key=level_sums.get)
    return result