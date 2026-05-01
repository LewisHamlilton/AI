import heapq

def pm(s): [print(r) for r in s]; print()
def pos(s, v): return next((i, j) for i in range(3) for j in range(3) if s[i][j] == v)
def h(s, g): return sum(abs(i-x) + abs(j-y) for i in range(3) for j in range(3) if s[i][j] for x, y in [pos(g, s[i][j])])

def moves(s):
    x, y = pos(s, 0)
    res = []
    for m, dx, dy in [("UP", -1, 0), ("DOWN", 1, 0), ("LEFT", 0, -1), ("RIGHT", 0, 1)]:
        if 0 <= x+dx < 3 and 0 <= y+dy < 3:
            n = [list(r) for r in s]
            n[x][y], n[x+dx][y+dy] = n[x+dx][y+dy], n[x][y]
            res.append((m, n))
    return res

def a_star(start, goal):
    heap, vis = [(h(start, goal), 0, start, [])], set()
    print("Initial State:"); pm(start)

    while heap:
        _, g, cur, path = heapq.heappop(heap)
        key = tuple(map(tuple, cur))
        if key in vis: continue
        vis.add(key)

        print(f"g(n) = {g}\nPossible states f(n) calculation:\n")

        if cur == goal:
            print("Goal State Reached"); pm(goal)
            return print(f"Total Moves: {g}\nPath: {' -> '.join(path)}")

        evals = []
        for m, s in moves(cur):
            if tuple(map(tuple, s)) not in vis:
                hn = h(s, goal)
                fn = g + 1 + hn
                evals.append((m, s, fn))
                print(f"Move {m:<5} : f(n) = {fn}  [g={g+1}, h={hn}]")

        if evals:
            best = min(evals, key=lambda x: x[2])
            print(f"\nSelected Move : {best[0]}\nMinimum f(n)  : {best[2]}\n\nBest State:")
            pm(best[1])
            for m, s, fn in evals: heapq.heappush(heap, (fn, g+1, s, path+[m]))

    print("No solution found.")

# MAIN
print("Enter Initial State:")
initial_state = [list(map(int, input().split())) for _ in range(3)]
print("\nEnter Goal State:")
goal_state = [list(map(int, input().split())) for _ in range(3)]
a_star(initial_state, goal_state)