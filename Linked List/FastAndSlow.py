from SinglyLinkedList import Node

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

# Sample linked list used for the fast and slow function
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

'''
Visual representation of the linked list:
   a  ->  b  ->  c  ->  d  ->  e
                 ^             |
                 |             v
                  <-    <-    <-
'''

this = Node('a')
Is = Node('b')
Not = Node('c')
a = Node('d')
cycle = Node('e')

this.next = Is
Is.next = Not
Not.next = a
a.next = cycle

'''
Visual representation of the linked list:
   a  ->  b  ->  c  ->  d  ->  e
'''

print(findLoop(first))
# Output: True
print(findLoop(this))
# Ouput: False

'''
142. Linked List Cycle II

(medium)

Given the head of a linked list, return the node where the cycle begins. If there is no 
cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached 
again by continuously following the next pointer. Internally, pos is used to denote the 
index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there 
is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.


Example 1:
Input: head = [a, b, c, d, e], pos = 2
Output: tail connects to node index 2
Explanation: There is a cycle in the linked list, where tail connects to the second node.
'''

def detectCycle(head):
    # if there is no list then return none
    if not head:
        return None
    # set slow and fast pointers equal to head
    slow = fast = head
    # while the fast pointer isn't none
    while fast and fast.next:
        # let slow travel normal speed
        slow = slow.next
        # let fast travel twice as fast
        fast = fast.next.next
        # if their is a cycle then break
        if fast == slow:
            break
    # if there is no cycle then return none
    else:
        return None
    # while the head does not equal to slow
    while head != slow:
        # move to the next pointer
        head = head.next
        slow = slow.next
    # return the head
    return head

print(detectCycle(first).data)
# Output: c
print(detectCycle(this))
# Output: None