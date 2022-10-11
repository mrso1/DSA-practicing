class Stack:
    def __init__(self):
        self.stack = []
    # List append method to add element
    def add(self, data):
        if data not in self.stack:
            self.stack.append(data)
            return True
        else:
            return False

    # List pop method to remove element
    def remove(self):
        if len(self.stack) <= 0:
            return "No elements in the stack"
        else:
            return self.stack.pop()

    def peek(self):
        return self.stack[-1]


new_stack = Stack()
new_stack.add("Mon")
new_stack.add("Tue")
new_stack.add("Wed")
new_stack.remove()
print(new_stack.peek())
