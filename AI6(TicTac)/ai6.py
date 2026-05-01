board, wins = [' ']*9, [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]

def show(): b = board; print(f"\n {b[0]}|{b[1]}|{b[2]}\n -+-+-\n {b[3]}|{b[4]}|{b[5]}\n -+-+-\n {b[6]}|{b[7]}|{b[8]}\n")
def win(): return next((board[i] for i,j,k in wins if board[i]==board[j]==board[k]!=' '), "Draw" if ' ' not in board else None)

def mm(is_m):
    w = win()
    if w: return {'O': 1, 'X': -1, 'Draw': 0}[w]
    sc = []
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O' if is_m else 'X'
            sc.append(mm(not is_m))
            board[i] = ' '
    return max(sc) if is_m else min(sc)

print("Positions: 0-8"); show()

while not win():
    m = int(input("Your move (0-8): "))
    if board[m] != ' ': print("Invalid!"); continue
    board[m] = 'X'; show()
    if not win():
        c = max(((mm(False), i) for i in range(9) if board[i] == ' '), key=lambda x: x[0])[1]
        board[c] = 'O'; print(f"Computer: {c}"); show()

r = win()
print("You Win" if r == 'X' else "Computer Wins" if r == 'O' else "Draw")

