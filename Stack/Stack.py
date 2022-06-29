# Stack class contains a stack list with methods
class Stack:
    stack = []
    # returns a string representation of the stack
    def __repr__(self) -> str:
        return str(self.stack)
    # this method adds an element to the top of the stack
    def push(self, data):
        self.stack.append(data)
    # this method removes and returns the item at the top of the stack
    def pop(self):
        return self.stack.pop()
    # this method returns True if the stack is empty, false if it is not
    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        return False
    # this method returns the item at the top of the stack
    def peek(self):
        return self.stack[len(self.stack) - 1]
    # this method returns the size of the stack
    def size(self):
        return len(self.stack)
    # this method returns the position of the data that is being searched
    def search(self, data):
        count = 1
        for i in self.stack:
            if i == data:
                return count
            count += 1
        return str(data) + " is not in the stack"
    # this method clears the stack
    def clear(self):
        self.stack.clear()
# Test Stack methods
if __name__ == "__main__":
    # instance of the stack variable
    s = Stack()
    # push, adds an item to the top of the stack
    s.push('Dog')
    s.push('Bird')
    s.push('Lion')
    s.push('Bear')
    s.push('Flamingo')
    # peek, returns the item at the top of the stack
    print(s.peek())
    
    print(s)
    # size, returns the size of the stack
    print(s.size())
    
    # pop, returns and removed the item at the top of the stack
    print(s.pop())
    # isEmpty, returns true or false if the stack is empty of not
    print(s.isEmpty())
    # search, returns the location of the searched item
    print(s.search('Cow'))

    print(s)
    print(s.peek())
    print(s.search('Dog'))

    # clear, removes every item from the stack
    s.clear()

    print(s.isEmpty())

'''
Sample Output:
 - Flamingo
 - ['Dog', 'Bird', 'Lion', 'Bear', 'Flamingo']
 - 5
 - Flamingo
 - False
 - Cow is not in the stack
 - ['Dog', 'Bird', 'Lion', 'Bear']
 - Bear
 - 1
 - True
'''

    