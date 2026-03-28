class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        
    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        return None

    def isEmpty(self):
        return len(self.stack) == 0

s = Stack()
s.push("A")
s.push("B")
s.push("C")
print(s.pop()) # Output: C (last in, first out)
print(s.pop())