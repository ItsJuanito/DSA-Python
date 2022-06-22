'''
This is module contains both a Node and a LinkedList class to create a signly linked list data structure.
A linked list is a linear data structure, in which the elements are not stored at contiguous memory locations.
In short, a linked list consists of nodes where each node contains a data field and a reference(link) to the 
next node in the list.
'''

# This class consists of a node object with data and a reference to the next node
class Node:
    # constructor method that sets node data and next
    def __init__(self, data=None):
        self.data = data
        self.next = None

# This class consists of making a linked list out of the Node's class
class LinkedList():
    # constructor method, adds a single node value with next = None
    def __init__(self, data):
        self.head = Node(data)
    
    # method that pushes a node at the beginning of the linked list
    def push(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    # method that appends a node at the end of the linked list
    def append(self, data):
        if self.head == None:
            return self.head
        current = self.head
        while current.next != None:
            current = current.next
        current.next = Node(data)

    # this method inserts a node into the linked list at a given index
    def insertAt(self, index, data):
        if self.head == None:
            return self.head
        current = self.head
        newNode = Node(data)
        count = 0
        while current != None:
            if count == index:
                break
            temp = current
            current = current.next
            count += 1
        temp.next = newNode
        newNode.next = current.next

    # this method deletes the node by the data
    def deleteNode(self, data):
        if self.head == None:
            return self.head
        current = self.head
        if current != None:
            if current.data == data:
                current.next = self.head
                current = None
                return
        while current != None:
            if current.data == data:
                break
            temp = current
            current = current.next
        if current == None:
            return
        temp.next = current.next
        current = None

    def deleteAt(self, index):
        if self.head == None:
            return self.head
        current = self.head
        if current != None:
            if index == 0:
                current.next = self.head
                current = None
                return
        count = 0
        while current != None:
            if count == index:
                break
            count += 1
            temp = current
            current = current.next
        if temp == None:
            return
        temp.next = current.next
        temp = None

    # this method returns or prints the length of the linked list
    def length(self):
        if self.head == None:
            return 0
        current = self.head
        count = 1
        while current.next != None:
            count += 1
            current = current.next
        return count

    # method that prints the datas in the linked list
    def print(self):
        if self.head == None:
            return self.head
        current = self.head
        string = ""
        while current != None:
            string += str(current.data) + "->"
            current = current.next
        string += "None"
        print(string)

    # how to reverse a linked list
    def reverse(self):
        prev = None
        current = self.head
        while current != None:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        # print the reversed linked list
        string = ""
        while prev != None:
            string += str(prev.data) + "->"
            prev = prev.next
        string += "None"
        print(string)


# Test the Linked List class and methods
if __name__ == '__main__':
    # instance of a LinkedList
    ll = LinkedList(2)
    ll.print()
    # append(), add a node to the end of the linked list
    ll.append(3)
    ll.append(8)
    ll.append(12)
    ll.print()
    # push(), add a node to the beginning of the linked list
    ll.push(1)
    ll.print()
    # insertAt(), add a node at a given index
    ll.insertAt(3, 100)
    ll.print()
    # deleteNode(), deletes a node by its value
    ll.deleteNode(100)
    ll.print()
    # deleteAt(), deletes a node at a given index
    ll.deleteAt(3)
    ll.print()
    # length(), returns the length of the linked list
    print(ll.length())
    # reverse(), prints out the reversed linked list
    sll = ll.reverse()
    
'''
Sample Outputs:
- 2->None
- 2->3->8->12->None
- 1->2->3->8->12->None
- 1->2->3->100->12->None
- 1->2->3->12->None
- 1->2->3->None
- 3
- 3->2->1->None
'''