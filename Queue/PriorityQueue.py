'''
Priority Queue is an abstract data type that is similar to a queue, and every element has 
some priority value associated with it. The priority of the elements in a priority queue 
determines the order in which elements are served. If in any case the elements have same 
priority, they are served as per their ordering in the queue.
'''
# Priority Queue class that contains a queue list and methods 
class PQueue:
    queue = []
    # this method checks to see if the priority queue is empty or not
    def isEmpty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False
    # this method adds an item to the priority queue
    def push(self, priority, data):
        if priority < 0:
            return print("Invalid priority entry!")
        temp = (priority, data)
        self.queue.append(temp)
    # this method removes and returns the prioritized value
    def pop(self):
        self.queue.sort(key=lambda q: q[0])
        data = self.queue[0][1]
        del self.queue[0]
        return data
    # this method prints the priority queue
    def print(self):
        self.queue.sort(key=lambda q: q[0])
        for tuple in self.queue:
            print(str(tuple[1]) + " ", end="")
        print()
# Test Priority Queue methods
if __name__ == "__main__":
    # instance of PQueue class
    pq = PQueue()
    # isEmpty, returns true if priority queue is empty, and false if it is not empty
    print(pq.isEmpty())
    # push, adds an item with a priority to the priority queue 
    pq.push(-1, 19)
    pq.push(10, 4)
    pq.push(1, 18)
    pq.push(3, 1)
    pq.push(1, 12)
    # print, simlpy prints the priority queue
    pq.print()
    # pop, returns and deleted the prioritized value
    popped = pq.pop()
    print(popped)
    print(pq.isEmpty())
    pq.print()

'''
Sample Output:
 - True
 - Invalid priority entry!
 - 18 12 1 4 
 - 18
 - False
 - 12 1 4 
'''