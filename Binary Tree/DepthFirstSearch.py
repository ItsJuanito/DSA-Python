import sys
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

'''
Tree Structre (a):
                5
             /     \
            2       8
          /  \     /  \
         1  None  6  None

Tree Strucutre (b):
                 7
             /       \
            5         10
          /   \     /   \
       None  None  9    None
'''

# this method returns a list of the tree using a depth first search (by subtree)
def depthFirstSearch(root):
    if root == None:
        return []
    result = []
    stack = Stack()
    stack.push(root)
    while stack.size() > 0:
        current = stack.pop()
        result.append(current.data)
        if current.right:
            stack.push(current.right)
        if current.left:
            stack.push(current.left)
    return result

print(depthFirstSearch(a))
# Output: [5, 2, 1, 8, 6]
print(depthFirstSearch(b))
# Output: [7, 5, 10, 9]