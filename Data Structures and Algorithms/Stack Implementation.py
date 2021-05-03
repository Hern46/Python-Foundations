class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop_item(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

s = Stack()

s.push('poop')
s.push(1)
s.push(True)
print(s.isEmpty())
print(s.pop_item())
print(s.pop_item())
print(s.peek())
print(s.size())
print(s.pop_item())
print(s.size())
print(s.isEmpty())