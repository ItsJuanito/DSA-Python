'''
A tree whose elements have at most 2 children is called a binary tree. Since each element 
in a binary tree can have only 2 children, we typically name them the left and right child.
This odule contains a TreeNode class which has references to its right and left children.
'''

# Tree Node class that contains a data variable and references to the left and right children
class TreeNode:
    # constructor method that sets left and right children as well as data
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    # this method adds a data node to the binary tree
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left == None:
                    self.left = TreeNode(data)
                else:
                    self.left.insert(data)
            if data > self.data:
                if self.right == None:
                    self.right = TreeNode(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
    # this method returns a list of the nodes in pre order
    def preOrderTraversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.preOrderTraversal(root.left)
            res = res + self.preOrderTraversal(root.right)
        return res
    # this method returns a list of the nodes in order
    def inOrderTraversal(self, root):
        res = []
        if root:
            res = res + self.inOrderTraversal(root.left)
            res.append(root.data)
            res = res + self.inOrderTraversal(root.right)
        return res
    # this method returns a list of the nodes in post order
    def postOrderTraversal(self, root):
        res = []
        if root:
            res = res + self.preOrderTraversal(root.left)
            res = res + self.preOrderTraversal(root.right)
            res.append(root.data)
        return res
    # this method prints the data nodes in the binary tree
    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data, end=" ")
        if self.right:
            self.right.printTree()

# Test Binary Tree Node Methods
if __name__ == "__main__":
    a = TreeNode(10)
    a.insert(4)
    a.insert(6)
    a.insert(12)
    a.printTree()
    print()

    print("Pre order: " + str(a.preOrderTraversal(a)))
    print("In order: " + str(a.inOrderTraversal(a)))
    print("Post order: " + str(a.postOrderTraversal(a)))

'''
Sample Output:
 - 4 6 10 12 
 - Pre order: [10, 4, 6, 12]
 - In order: [4, 6, 10, 12]
 - Post order: [4, 6, 12, 10]
 - [10, 4, 6, 12]

 Tree Structure:
          10
       /      \
      4       12
    /   \    /   \
  None   6 None  None
'''