class Node:

    def __init__(self, value):
        self.value = value
        self.nextnode = None

a = Node(2)
b = Node(2)
c = Node(2)

a.nextnode = b
b.nextnode = c
c.nextnode = a

x = Node(5)
y = Node(5)
z = Node(5)

x.nextnode = y
y.nextnode = z


def cycle_check(node):
    node_list = []
    while node != None:
        node_list.append(node)
        node = node.nextnode
        if node in node_list:
            return True

    return False

print(cycle_check(x))