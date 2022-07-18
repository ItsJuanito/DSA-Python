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
    # set slow pointer to the head
    slow = head
    # set fast pointer to the head
    fast = head
    # loop through the linked list
    while (slow and fast and fast.next):
        # slow will move linear
        slow = slow.next
        # fast moves twice as fast as slow
        fast = fast.next.next
        # if there is a loop then return True
        if slow == fast:
            return True
    # if there was no loop present, then return false
    return False

print(findLoop(first))