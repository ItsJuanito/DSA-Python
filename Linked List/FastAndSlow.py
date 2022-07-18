from SinglyLinkedList import Node

first = Node('a')
second = Node('b')
third = Node('c')
fourth = Node('d')
fifth = Node('e')
sixth = Node('f')

first.next = second
second.next = third
third.next = fourth
fourth.next = fifth
fifth.next = sixth
sixth.next = third

# this function uses the fast and slow approach to see if there is a loop in the linked list
def findLoop(head):
    slow = head
    fast = head
    while (slow and fast and fast.next):
        slow = slow.next
        fast = fast.next
        if slow == fast:
            return True

print(findLoop(first))