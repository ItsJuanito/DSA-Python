class Queue:
    queue = []
    def __repr__(self) -> str:
        return str(self.queue)
    def enqueue(self, data):
        self.queue.insert(0, data)

    def dequeue(self):
        return self.queue.pop()
    
    def size(self):
        return len(self.queue)
    
    def peek(self):
        return self.queue[len(self.queue) - 1]
    
    def isEmpty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False

if __name__ == "__main__":
    q = Queue()
    
    print(q.isEmpty())
    
    q.enqueue(10)
    q.enqueue(3)
    q.enqueue(24)
    q.enqueue(6)
    q.enqueue(11)

    print(q)
    
    print(q.dequeue())
    
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