'''
A Queue is a linear structure which follows a particular order in which the operations 
are performed. The order is First In First Out (FIFO). A good example of a queue is any 
queue of consumers for a resource where the consumer that came first is served first. 
The difference between stacks and queues is in removing. In a stack we remove the item 
the most recently added; in a queue, we remove the item the least recently added.
'''

# Queue class contains a queue list and methods
class Queue:
    queue = []
    # this method returns the string values of the queue
    def __repr__(self) -> str:
        return str(self.queue)
    # this method adds data to the queue
    def enqueue(self, data):
        self.queue.insert(0, data)
    # this method returns and deletes the last value in the queue
    def dequeue(self):
        return self.queue.pop()
    # this method returns the size of the queue
    def size(self):
        return len(self.queue)
    # this method returns the last element(tail) in the queue
    def peek(self):
        return self.queue[len(self.queue) - 1]
    # this method returns true if the queue is empty and false if it is not
    def isEmpty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False

if __name__ == "__main__":
    # instance of Queue class
    q = Queue()
    # isEmpty, returns true of queue is empty, false if it is not
    print(q.isEmpty())
    # enqueue, adds an element to the queue
    q.enqueue(10)
    q.enqueue(3)
    q.enqueue(24)
    q.enqueue(6)
    q.enqueue(11)

    print(q)
    # dequeue, removes the last element in the queue
    print(q.dequeue())
    # returns the last element of the queue
    print(q.peek())
    
    print(q.isEmpty())
    
    q.enqueue(18)
    print(q)

'''
Sample Output:
 - True
 - [11, 6, 24, 3, 10]
 - 10
 - 3
 - False
 - [18, 11, 6, 24, 3]
'''