'''
This is module contains both a Node and a LinkedList class to create a doubly linked list data 
structure. A Doubly Linked List (DLL) contains an extra pointer, typically called the previous 
pointer, together with next pointer and data which are there in singly linked list. 
'''
# This class consists of a node object with data and a reference to the previous and next nodes
class Node:
    # constructor method that sets prev, data, and next values
    def __init__(self, data=None):
        self.prev = None
        self.data = data
        self.next = None

# This class consists of making a linked list out of the Node's class
class LinkedList:
    # constructor method that sets an instance of a node object to the head
    def __init__(self, data):
        self.head = Node(data)

    # this method adds an element to the beginning of the linked list
    def push(self, data):
        newNode = Node(data)
        if self.head == None:
            return self.head
        current = self.head
        current.prev = newNode
        newNode.next = current
        self.head = newNode

    # this method adds an element to the end of the linked list
    def append(self, data):
        newNode = Node(data)
        if self.head == None:
            return self.head
        current = self.head
        while current.next != None:
            current = current.next
        current.next = newNode
        newNode.prev = current

    # this method adds an element after the given node data
    def insertAfter(self, node_data, data):
        if self.head == None:
            return self.head
        current = self.head
        newNode = Node(data)
        while current.next != None:
            if current.data == node_data:
                break
            current = current.next
        newNode.next = current.next
        newNode.prev = current
        current.next = newNode
        current.next.prev = newNode

    # this method adds a node at a given index
    def insertAt(self, index, data):
        if self.head == None:
            return self.head
        current = self.head
        count = 0
        while current != None:
            if count == index:
                break
            count += 1
            current = current.next
        current.data = data

    # this method returns the data of the given index
    def get(self, index):
        if self.head == None:
            return self.head
        count = 0
        current = self.head
        while current.next != None:
            if count == index:
                return current.data
            count += 1
            current = current.next
        return 'Index does not exist!'

    # this method deletes a node by the given data
    def deleteNode(self, data):
        if self.head == None:
            return self.head
        current = self.head
        while current.next != None:
            if current.data == data:
                break
            previous = current
            current = current.next
        if current == None:
            return
        previous.next = current.next
        current.next.prev = previous
        current = None

    # this method deletes a node by the given index
    def deleteIndex(self, index):
        if self.head == None:
            return self.head
        current = self.head
        count = 0
        while current.next != None:
            if count == index:
                break
            count += 1
            previous = current
            current = current.next
        previous.next = current.next
        current.next.prev = previous
        current = None

    # this method returns the length of the list
    def length(self):
        length = 0
        if self.head == None:
            return length
        current = self.head
        while current != None:
            length += 1
            current = current.next
        return length

    # this method prints the linked list forwards
    def print_foward(self):
        if self.head == None:
            print("None")
        string = "None<->"
        current = self.head
        while current != None:
            string += str(current.data) + "<->"
            current = current.next
        string += "None"
        print(string)
        
    # this method prints the linked list bakwards
    def print_backward(self):
        if self.head == None:
            print("None")
        string = "None<->"
        current = self.head
        while current.next != None:
            current = current.next
        tail = current
        while tail != None:
            string += str(tail.data) + "<->"
            tail = tail.prev
        string += "None"
        print(string)
        
# Test the Linked List class and methods
if __name__ == "__main__":
    # instance of Linked List object
    ll = LinkedList(10)
    # append(), add a node to the end of the linked list
    ll.append(21)
    ll.append(18)
    # print_forward(), prints the linked list in the forward position
    ll.print_foward()
    # push(), adds a node to the front of the linked list
    ll.push(5)
    ll.push(1)
    ll.print_foward()
    # insertAfter(), allows you to insert a node after a given node
    ll.insertAfter(5, 55)
    ll.print_foward()
    # insertAt(), adds a node at the given index
    ll.insertAt(2, 11)
    ll.print_foward()
    # deleteNode(), deletes a node by its data
    ll.deleteNode(11)
    ll.print_foward()
    # deleteIndex(), deletes the node at the given index
    ll.deleteIndex(1)
    ll.print_foward()
    # print_backward(), prints the linked list in reverse
    ll.print_backward()
    # get(), returns the node data by the given index
    print(ll.get(4))
    print(ll.get(2))
    # length(), return the length of the linked list
    print("Length: " + str(ll.length()))
'''
Sample Outputs:
- None<->10<->21<->18<->None
- None<->1<->5<->10<->21<->18<->None
- None<->1<->5<->55<->10<->21<->18<->None
- None<->1<->5<->11<->10<->21<->18<->None
- None<->1<->5<->10<->21<->18<->None
- None<->1<->10<->21<->18<->None
- None<->18<->21<->10<->1<->None
- Index does not exist!
- 21
- Length: 4
'''