class Deque:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def add_front(self, item):
        self.items.append(item)

    def add_rear(self, item):
        self.items.insert(0, item)

    def remove_front(self):
        return self.items.pop()

    def remove_rear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

d = Deque()
d.add_front('middle')
d.add_front('front')
d.add_rear('rear')
print(d.size())
print(d.isEmpty())
print(d.remove_front())
print(d.remove_rear())
print(d.size())
print(d.remove_rear())
print(d.isEmpty())