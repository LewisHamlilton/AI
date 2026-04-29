def idx(x): return nodes.index(x) if x in nodes else -1
def show(lst): return '[' + ', '.join(nodes[i] for i in lst) + ']'

def traverse(start, end, mode):
    i, j = idx(start), idx(end)
    if -1 in (i, j): return print("Invalid node!")
    
    vis, op, cl = [False]*vertices, [i], []
    print(f"\n{mode} Traversal:\n{'OPEN':<30} {'X':<10} CLOSED\n" + "-"*62)
    
    while op:
        curr_op = show(op)
        x = op.pop(0) if mode == "BFS" else op.pop()
        cl.append(x)
        vis[x] = True
        print(f"{curr_op:<30} {nodes[x]:<10} {show(cl)}")
        
        if x == j: break
        
        rng = range(vertices) if mode == "BFS" else range(vertices-1, -1, -1)
        for i in rng:
            if adj[x][i] and not vis[i]:
                vis[i] = True
                op.append(i)
    
    print(f"\nFinal Path: {show(cl)}\n")

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
    ch = input("\n--- MENU ---\n1. BFS\n2. DFS\n3. Exit\nEnter choice: ").strip()
    if ch == '3': break
    if ch in ('1', '2'):
        traverse(input("Start node: "), input("End node: "), "BFS" if ch == '1' else "DFS")
    else:
        print("Invalid choice!")