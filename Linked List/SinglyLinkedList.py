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
        # store data member variable
        self.data = data
        # set next reference equal to None 
        self.next = None
# This class consists of making a linked list out of the Node's class
class LinkedList():
    # constructor method, adds a single node value with next = None
    def __init__(self, data):
        # create an instance of Node object
        self.head = Node(data)
    
    # method that pushes a node at the beginning of the linked list
    def push(self, data):
        # create instance of a new node
        newNode = Node(data)
        # set the next data equal to the first value of the linked list
        newNode.next = self.head
        # let the head point to the newNode (makes the newNode the first node)
        self.head = newNode

    # method that appends a node at the end of the linked list
    def append(self, data):
        # if head is empty then return None
        if self.head == None:
            return self.head
        # store head node
        current = self.head
        # loop through current linked list until we get to the end
        while current.next != None:
            # proceed to the next node
            current = current.next
        # set last node equal to the appended node data
        current.next = Node(data)

    # this method inserts a node into the linked list at a given index
    def insertAt(self, index, data):
        # if head is empty then return None
        if self.head == None:
            return self.head
        # store head node
        current = self.head
        # create new node
        newNode = Node(data)
        # set counter variable
        count = 0
        # loop through the linked list until index is found
        while current != None:
            # check to see if the count is equal to the index, then break out of the loop
            if count == index:
                break
            # set temp equal to the current node
            temp = current
            # proceed to the next node
            current = current.next
            # increase count by one
            count += 1
        # set the next node equal to the new node
        temp.next = newNode
        # set new node's next to the original next of current
        newNode.next = current.next

    # this method deletes the node by the data
    def deleteNode(self, data):
        # if head is empty then return None
        if self.head == None:
            return self.head
        # store head node
        current = self.head
        # check to see if the linked list is not empty
        if current != None:
            # if the data matches the current data (first value) then delete it
            if current.data == data:
                # setting second node equal to the head node
                current.next = self.head
                current = None
                return
        # loop through the linked list to find the data
        while current != None:
            # if the data is equal to the current data then we break out of the loop
            if current.data == data:
                break
            # set a temperary node equal to the current node to keep track of the previous node
            temp = current
            # proceed to the next node
            current = current.next
        # if the current node is none then nothing gets done
        if current == None:
            return
        # unlink the node form the linked list
        temp.next = current.next
        current = None

    # this method deletes a node at a given index
    def deleteAt(self, index):
        # if the first node is none then simply return it
        if self.head == None:
            return self.head
        # set current equal to the head node
        current = self.head
        # if the node is not empty run the following code
        if current != None:
            # if the index is the first node then delete that node
            if index == 0:
                # set the second node equal to the head(first node)
                current.next = self.head
                # set the old head node to none
                current = None
                return
        # set a counter variable
        count = 0
        while current != None:
            # if the count is equal to the index we're looking for then break out of the loop to delete the node
            if count == index:
                break
            # increment count by 1
            count += 1
            # set a temperary node equal to the current node to keep track of the previous node
            temp = current
            # proceed to the next node
            current = current.next
        # if the current node is none then nothing gets done
        if temp == None:
            return
        # unlink the node form the linked list
        temp.next = current.next
        temp = None

    # this method returns or prints the length of the linked list
    def length(self):
        # if head is empty then return None
        if self.head == None:
            return 0
        # store head node
        current = self.head
        # set counter variable
        count = 1
        # loop through current linked list until we get to the end
        while current.next != None:
            # incriment count by 1
            count += 1
            # proceed to next node
            current = current.next
        # return or print count (optional)
        return count

    # method that prints the datas in the linked list
    def print(self):
        # if head is empty then return None
        if self.head == None:
            return self.head
        # store head node
        current = self.head
        # create an empty string 
        string = ""
        # loop through the linked list until it reaches the None data
        while current != None:
            # append the data to the string
            string += str(current.data) + "->"
            # proceed to the next node
            current = current.next
        # append the 'None' string
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

'''
Sample Outputs:
- 2->None
- 2->3->8->12->None
- 1->2->3->8->12->None
- 1->2->3->100->12->None
- 1->2->3->12->None
- 1->2->3->None
- 3
'''