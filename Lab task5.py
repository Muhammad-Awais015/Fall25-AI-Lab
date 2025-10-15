tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': ['G'],
    'G': []
    
}

def dfs_stack(start, goal):
    visited = []
    stack = [start]

    while stack:
        current = stack.pop()
        if current not in visited:
            visited.append(current)
            print("Visiting:", current)
            if current == goal:
                print("Goal:", goal, "found!") 
                return visited
            for child in reversed(tree[current]):
                if child not in visited:
                    stack.append(child)

    print("Goal:", goal, "not found.")
    return visited

visited_nodes = dfs_stack('A', 'D')
print("DFS Traversal:", visited_nodes)
