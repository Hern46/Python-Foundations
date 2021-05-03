class Vertex:

    def __init__(self, key):
        self.id = key
        self.connected_to = {}

    def add_neighbor(self,nbr,weight):
        self.connected_to[nbr] = weight

    def get_connections(self):
        return self.connected_to.keys()

    def get_weight(self, nbr):
        return self.connected_to[nbr]

    def get_id(self):
        return self.id

    def __str__(self):
        return f'{self.id} is connected to {[x.id for x in self.connected_to]}'

class Graph:

    def __init__(self):
        self.vert_list = {}
        self.num_vertices = 0

    def add_vertex(self, key):
        self.num_vertices += 1
        new_vert = Vertex(key)
        self.vert_list[key] = new_vert
        return new_vert

    def add_edge(self, f, t, cost=0):
        if f not in self.vert_list:
            self.add_vertex(f)
        if t not in self.vert_list:
            self.add_vertex(t)

        self.vert_list[f].add_neighbor(self.vert_list[t], cost)

    def get_vertex(self, n):
        if n in self.vert_list:
            return self.vert_list[n]
        else:
            return None

    def get_vertices(self):
        return self.vert_list.keys()

    def __contains__(self, item):
        return item in self.vert_list

    def __iter__(self):
        return iter(self.vert_list.values())

    def __str__(self):
        return f'{self.vert_list}'

g = Graph()

for i in range(6):
    g.add_vertex(i)

#for i in range(1,6):
 #   g.add_edge(i-1, i, 99)
  #  g.add_edge(6-i, i, 500)
   # g.add_edge(6-i, i-1, 60000)
    #if i != 5:
     #   g.add_edge(i-1,i+1, 3232)
#for i in range(6):
 #   g.add_edge(0, i, 60)


#for i in range(6):
 #   print(g.get_vertex(i))

for key in g.get_vertices():
    print(g.get_vertex(key))

