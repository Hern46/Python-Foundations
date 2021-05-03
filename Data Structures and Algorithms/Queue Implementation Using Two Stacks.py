class Queue2Stacks:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, element):
        self.stack1.append(element)

    def dequeue(self):
        if self.stack2 == []:
            while self.stack1 != []:
                self.stack2.append(self.stack1.pop())

        return self.stack2.pop()

q = Queue2Stacks()

for i in range(5):
    q.enqueue(i)

for i in range(5):
    print(q.dequeue())

q.enqueue(10)
q.enqueue(20)
print(q.dequeue())
q.enqueue(30)
print(q.dequeue())
print(q.dequeue())
