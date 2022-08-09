import sys
from BinaryTree import TreeNode

sys.path.append('..')
from Stack.Stack import Stack

a = TreeNode()
a.insert(5)
a.insert(2)
a.insert(1)
a.insert(8)
a.insert(6)

b = TreeNode()
b.insert(7)
b.insert(10)
b.insert(9)
b.insert(5)

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

