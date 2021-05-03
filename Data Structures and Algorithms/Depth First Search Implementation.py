graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

def dfs(graph, start):
    visited = set()
    stack = [start]

    while stack:
        vertex = stack.pop()

        if vertex not in visited:
            visited.add(vertex)

            stack.extend(graph[vertex] - visited)

    return visited

print(dfs(graph, 'A'))

def dfs_recursive(graph, start, visited=None):

    if visited == None:
        visited = set()
    visited.add(start)
    for nxt in graph[start] - visited:
        dfs_recursive(graph, nxt, visited)
    return visited

print(dfs_recursive(graph, 'A'))

def dfs_paths(graph, start, goal):
    stack = [(start, [start])]

    while stack:
        vertex, path = stack.pop()

        for nxt in graph[vertex] - set(path):
            if nxt == goal:
                yield path + [nxt]
            else:
                stack.append((nxt, path + [nxt]))

print(list(dfs_paths(graph, 'B', 'E')))