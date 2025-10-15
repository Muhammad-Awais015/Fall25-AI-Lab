from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

def bfs_with_nodes(start, goal):
    visited = []
    queue = deque([start]) 

    while queue:
        current = queue.popleft()
        if current not in visited:
            print("Visiting:", current.value)
            visited.append(current)
            if current.value == goal:
                print("Goal:", goal, "found!")
                return [node.value for node in visited]
            for child in current.children:
                if child not in visited:
                    queue.append(child)

    print("Goal:", goal, "not found.")
    return [node.value for node in visited]

A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')
E = Node('E')
F = Node('F')
G = Node('G')

A.children = [B, C]
B.children = [D, E]
C.children = [F]
F.children = [G]

visited_nodes = bfs_with_nodes(A, 'D')
print("BFS Traversal:", visited_nodes)
