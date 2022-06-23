class PQueue:
    queue = []
    def isEmpty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False
    
    def push(self, priority, data):
        if priority < 0:
            return print("Invalid priority entry!")
        temp = (priority, data)
        self.queue.append(temp)

    def pop(self):
        self.queue.sort(key=lambda q: q[0])
        data = self.queue[0][1]
        del self.queue[0]
        return data

    def print(self):
        self.queue.sort(key=lambda q: q[0])
        for tuple in self.queue:
            print(str(tuple[1]) + " ", end="")
        print()

if __name__ == "__main__":
    pq = PQueue()
    print(pq.isEmpty())
    pq.push(-1, 19)
    pq.push(10, 4)
    pq.push(1, 18)
    pq.push(3, 1)
    pq.push(1, 12)

    pq.print()

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