class Queue:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

q = Queue()

q.enqueue(4)
q.enqueue(5)
q.enqueue(6)
print(q.dequeue())
print(q.size())
print(q.isEmpty())