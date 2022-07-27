import sys
from BinaryTree import TreeNode

sys.path.append('..')
from Queue.Queue import Queue

a = TreeNode(10)
a.insert(4)
a.insert(6)
a.insert(12)

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

