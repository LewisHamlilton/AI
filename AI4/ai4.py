def idx(x):
    return nodes.index(x) if x in nodes else -1

def show(lst):
    return '[' + ', '.join(nodes[i] for i in lst) + ']'

def traverse(start, end, mode):
    visited = [False]*vertices
    open_list = [idx(start)]
    closed = []
    
    if open_list[0] == -1 or idx(end) == -1:
        print("Invalid node!")
        return
    
    print(f"\n{mode} Traversal:")
    print(f"{'OPEN':<30} {'X':<10} CLOSED")
    print("-"*62)
    
    while open_list:
        current_open = show(open_list)
        
        x = open_list.pop(0) if mode == "BFS" else open_list.pop()
        closed.append(x)
        visited[x] = True
        
        print(f"{current_open:<30} {nodes[x]:<10} {show(closed)}")
        
        if x == idx(end):
            break
        
        rng = range(vertices) if mode == "BFS" else range(vertices-1, -1, -1)
        
        for i in rng:
            if adj[x][i] and not visited[i]:
                visited[i] = True
                open_list.append(i)
    
    print(f"\nFinal Path: {show(closed)}\n")


# MAIN
vertices = int(input("Enter number of vertices: "))
nodes = input("Enter node names: ").split()
adj = [[0]*vertices for _ in range(vertices)]

e = int(input("Enter number of edges: "))
print("Enter edges:")
for _ in range(e):
    a, b = input().split()
    if a in nodes and b in nodes:
        i, j = idx(a), idx(b)
        adj[i][j] = adj[j][i] = 1
    else:
        print("Invalid edge ignored")

while True:
    print("\n--- MENU ---")
    print("1. BFS\n2. DFS\n3. Exit")
    ch = int(input("Enter choice: "))
    
    if ch == 3:
        break
    
    s = input("Start node: ")
    d = input("End node: ")
    
    if ch == 1:
        traverse(s, d, "BFS")
    elif ch == 2:
        traverse(s, d, "DFS")
    else:
        print("Invalid choice!")