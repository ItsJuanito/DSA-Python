class Node:
    def __init__(self, data=None):
        self.prev = None
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, data):
        self.head = Node(data)
    
    def push(self, data):
        newNode = Node(data)
        if self.head == None:
            return self.head
        current = self.head
        current.prev = newNode
        newNode.next = current
        self.head = newNode

    def append(self, data):
        newNode = Node(data)
        if self.head == None:
            return self.head
        current = self.head
        while current.next != None:
            current = current.next
        current.next = newNode
        newNode.prev = current

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
    
    def updateIndex(self, index, data):
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
        

    def length(self):
        length = 0
        if self.head == None:
            return length
        current = self.head
        while current != None:
            length += 1
            current = current.next
        return length

    def print(self):
        if self.head == None:
            print("None")
        string = "None<->"
        current = self.head
        while current != None:
            string += str(current.data) + "<->"
            current = current.next
        string += "None"
        print(string)

if __name__ == "__main__":
    ll = LinkedList(10)
    ll.append(21)
    ll.append(18)
    ll.print()

    ll.push(5)
    ll.push(1)
    ll.print()
    
    ll.insertAfter(5, 55)
    ll.print()

    ll.updateIndex(2, 11)
    ll.print()


    ll.deleteNode(11)
    ll.print()
    
    ll.deleteIndex(1)
    ll.print()

    print(ll.get(4))
    print(ll.get(2))

    print("Length: " + str(ll.length()))

'''
Sample Outputs:
- None<->10<->21<->18<->None
- None<->1<->5<->10<->21<->18<->None
- None<->1<->5<->55<->10<->21<->18<->None
- None<->1<->5<->11<->10<->21<->18<->None
- None<->1<->5<->10<->21<->18<->None
- None<->1<->10<->21<->18<->None
- Index does not exist!
- 21
- Length: 4
'''