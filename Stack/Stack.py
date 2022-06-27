class Stack:
    stack = []
    def __repr__(self) -> str:
        return str(self.stack)
    def push(self, data):
        self.stack.append(data)
    def pop(self):
        return self.stack.pop()
    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        return False
    def peek(self):
        return self.stack[len(self.stack) - 1]
    def search(self, data):
        count = 1
        for i in self.stack:
            if i == data:
                return count
            count += 1
        return str(data) + " is not in the stack"
    def clear(self):
        self.stack.clear()

if __name__ == "__main__":
    s = Stack()

    s.push('Dog')
    s.push('Bird')
    s.push('Lion')
    s.push('Bear')
    s.push('Flamingo')

    print(s.peek())

    print(s)

    print(s.pop())

    print(s.isEmpty())

    print(s.search('Cow'))

    print(s)

    print(s.peek())

    print(s.search('Dog'))

    s.clear()

    print(s.isEmpty())

'''
Sample Output:
 - Flamingo
 - ['Dog', 'Bird', 'Lion', 'Bear', 'Flamingo']
 - Flamingo
 - False
 - Cow is not in the stack
 - ['Dog', 'Bird', 'Lion', 'Bear']
 - Bear
 - 1
 - True
'''

    