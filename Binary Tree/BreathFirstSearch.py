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
print(breathFirstSearch(b))


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
print(levelBFS(b))