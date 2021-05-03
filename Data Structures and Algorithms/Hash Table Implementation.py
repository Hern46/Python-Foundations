class HashTable:

    def __init__(self, size):
        self.size = size
        self.slots = [None]*self.size
        self.data = [None]*self.size

    def length(self):
        count = 0
        for element in self.slots:
            if element != None:
                count += 1
        return count

    def __len__(self):
        return self.length()

    def hashfunction(self, key, size):
        return key % size

    def rehash(self, oldhash, size):
        return (oldhash + 1) % size

    def put(self, key, data):
        position = self.hashfunction(key, self.size)

        if self.slots[position] == None:
            self.slots[position] = key
            self.data[position] = data

        elif self.slots[position] == key:
            self.data[position] = data

        else:
            nextslot = self.rehash(position, self.size)

            while self.slots[nextslot] != None and self.slots[nextslot] != key:
                nextslot = self.rehash(nextslot, self.size)

            if self.slots[nextslot] == None:
                self.slots[nextslot] = key
                self.data[nextslot] = data

            else:
                self.data[nextslot] = data

    def __setitem__(self, key, data):
        return self.put(key, data)

    def get(self, key):
        start = self.hashfunction(key, self.size)

        data = None
        found = False
        stop = False

        position = start

        while self.slots[position] != None and not found and not stop:

            if self.slots[position] == key:
                data = self.data[position]
                found = True
            else:
                position = self.rehash(position, self.size)
                if position == start:
                    stop = True

        return data

    def __getitem__(self, key):
        return self.get(key)


h = HashTable(10)

h[1] = 'one'
h[2] = 'two'
h[3] = 'three'


print(h[2])
print(h.slots)