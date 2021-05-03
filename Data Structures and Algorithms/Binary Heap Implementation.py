class BinHeap:

    def __init__(self):
        self.heaplist = [0]
        self.currentsize = 0

    def perc_up(self, i):

        while i//2 > 0:
            if self.heaplist[i] < self.heaplist[i//2]:
                tmp = self.heaplist[i//2]
                self.heaplist[i//2] = self.heaplist[i]
                self.heaplist[i] = tmp
            i = i//2

    def insert(self, k):
        self.heaplist.append(k)
        self.currentsize += 1
        self.perc_up(self.currentsize)

    def min_child(self, i):

        if i*2 + 1 > self.currentsize:
            return i * 2
        else:
            if self.heaplist[i*2] < self.heaplist[i*2 + 1]:
                return i*2
            else:
                return i*2 + 1

    def perc_down(self, i):

        while i*2 <= self.currentsize:
            mc = self.min_child(i)
            if self.heaplist[i] > self.heaplist[mc]:
                tmp = self.heaplist[i]
                self.heaplist[i] = self.heaplist[mc]
                self.heaplist[mc] = tmp
            i = mc

    def show_min(self):
        return self.heaplist[1]

    def del_min(self):
        tmp = self.heaplist[1]
        self.heaplist[1] = self.heaplist[self.currentsize]
        self.currentsize -= 1
        self.heaplist.pop()
        self.perc_down(1)
        return tmp

    def build_heap(self, alist):

        i = len(alist)//2
        self.currentsize = len(alist)
        self.heaplist = [0] + alist
        while i > 0:
            self.perc_down(i)
            i -= 1

    def show_heap(self):
        print(self.heaplist[1:])

mylist = [2,3,1,5,4]

a = BinHeap()

a.build_heap(mylist)

print(a.show_min())
a.show_heap()
print(a.del_min())
a.show_heap()
a.insert(6)
a.show_heap()
a.insert(1)
a.show_heap()

