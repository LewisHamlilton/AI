import heapq
import copy

def print_matrix(s):
    for r in s: print(r)
    print()

def pos(state, val):
    for i in range(3):
        for j in range(3):
            if state[i][j] == val:
                return i, j

def h(state, goal):
    return sum(abs(i - x) + abs(j - y)
        for i in range(3) for j in range(3)
        if state[i][j] != 0
        for x, y in [pos(goal, state[i][j])])

def moves(state):
    x, y = pos(state, 0)
    dirs = [("UP", -1, 0), ("DOWN", 1, 0), ("LEFT", 0, -1), ("RIGHT", 0, 1)]
    
    res = []
    for m, dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new = copy.deepcopy(state)
            new[x][y], new[nx][ny] = new[nx][ny], new[x][y]
            res.append((m, new))
    return res

def a_star(start, goal):
    heap = [(h(start, goal), 0, start, [])]
    visited = set()

    print("Initial State:")
    print_matrix(start)

    while heap:
        f, g, cur, path = heapq.heappop(heap)
        key = tuple(map(tuple, cur))
        
        if key in visited: 
            continue
        visited.add(key)

        print(f"g(n) = {g}")
        print("Possible states f(n) calculation:\n")

        if cur == goal:
            print("Goal State Reached")
            print_matrix(goal)
            print(f"Total Moves: {g}")
            print("Path:", " -> ".join(path))
            return

        evals = []
        for m, s in moves(cur):
            k = tuple(map(tuple, s))
            if k not in visited:
                hn = h(s, goal)
                fn = g + 1 + hn
                evals.append((m, s, fn))
                print(f"Move {m:<5} : f(n) = {fn}  [g={g+1}, h={hn}]")

        if not evals: 
            continue

        best = min(evals, key=lambda x: x[2])
        print(f"\nSelected Move : {best[0]}")
        print(f"Minimum f(n)  : {best[2]}")
        print("\nBest State:")
        print_matrix(best[1])

        for m, s, fn in evals:
            heapq.heappush(heap, (fn, g+1, s, path+[m]))

    print("No solution found.")


# MAIN
print("Enter Initial State:")
initial_state = [list(map(int, input().split())) for _ in range(3)]

print("\nEnter Goal State:")
goal_state = [list(map(int, input().split())) for _ in range(3)]

a_star(initial_state, goal_state)