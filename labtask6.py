tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': ['G'],
    'G': []
}

def bfs_simple(start, goal):
    visited = []
    queue = [start] 

    while queue:
        current = queue.pop(0) 
        if current not in visited:
            print("Visiting:", current)
            visited.append(current)
            if current == goal:
                print("Goal:", goal, "found!")
                return visited
            for child in tree[current]:
                if child not in visited:
                    queue.append(child)

    print("Goal:", goal, "not found.")
    return visited

visited_nodes = bfs_simple('A', 'D')
print("BFS Traversal:", visited_nodes)
