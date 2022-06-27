'''
This module is composed of algorithms used for singly linked list.
'''
# import the "Node" object from the "SinglyLinkedList" module
from SinglyLinkedList import Node

# Default Linked List
########################
a = Node(10)
b = Node(6)
c = Node(23)
d = Node(15)

a.next = b
b.next = c
c.next = d

e = Node(11)
f = Node(7)

e.next = f
########################

# this function reverses a linked list
def reverse(head):
    if head == None:
        print_list(None)
    current = head
    prev = None
    while current != None:
        temp = current.next
        current.next = prev
        prev = current
        current = temp
    print_list(prev)
# this function prints the linked list
def print_list(head):
    if head == None:
        print("None")
    current = head
    string = ""
    while current != None:
        string += str(current.data) + "->"
        current = current.next
    string += "None"
    print(string)
# this function returns the sum of the linked list
def sum_of_list(head):
    sum = 0
    if head == None:
        return sum
    current = head
    while current != None:
        sum += current.data
        current = current.next
    return sum    
# this function returns True or False whether or not the data is in the linked list
def target_value(head, target):
    if head == None:
        return False
    current = head
    while current != None:
        if target == current.data:
            return True
        current = current.next
    return False
# this function adds two linked lists into one cronologically. 
def zipper_list(first, second):
    if first == None:
        return second
    elif second == None:
        return first
    newNode = None
    while first != None or second != None:
        if first != None:
            newNode = first
            print(str(newNode.data) + "->", end="")
            first = first.next
        if second != None:
            newNode = second
            print(str(newNode.data) + "->", end="")
            second = second.next
    print("None")

# Test linked list functions
if __name__ == "__main__":
    # print_list(), simply prints the list
    print_list(a)
    # sum_of_list(), returns the sum of a linked list
    print(sum_of_list(a))
    # target_value(), returns T or F if target exists or not
    print(target_value(a, 10))
    print(target_value(a, 7))
    # zipper_list(), creates a new linked list out of two existing linked list
    zipper_list(a, e)
    # reverse(), reverses a linked list
    reverse(a)

'''
Sample Outputs:
 - 10->6->23->15->None
 - 54
 - True
 - False
 - 10->11->6->7->23->15->None
 - 15->23->6->10->None
'''