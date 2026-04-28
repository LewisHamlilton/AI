import random

board = [' '] * 9
wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]

def print_board():
    r = board
    print(f"\n {r[0]}|{r[1]}|{r[2]}\n -+-+-\n {r[3]}|{r[4]}|{r[5]}\n -+-+-\n {r[6]}|{r[7]}|{r[8]}\n")

def winner():
    for i,j,k in wins:
        if board[i] == board[j] == board[k] != ' ': return board[i]
    return "Draw" if ' ' not in board else None

def minimax(is_max):
    result = winner()
    if result == 'O': return 1
    if result == 'X': return -1
    if result == "Draw": return 0

    scores = []
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O' if is_max else 'X'
            scores.append((minimax(not is_max), i))
            board[i] = ' '

    return max(scores)[0] if is_max else min(scores)[0]

def best_move():
    return max(
        ((minimax(False), i) for i in range(9) if board[i] == ' '),
        key=lambda x: x[0]
    )[1]

print("Positions: 0-8"); print_board()

while not winner():
    move = int(input("Your move (0-8): "))
    if board[move] != ' ': print("Invalid!"); continue
    board[move] = 'X'; print_board()
    if not winner():
        comp = best_move(); board[comp] = 'O'
        print(f"Computer: {comp}"); print_board()

r = winner()
print("You Win" if r == 'X' else "Computer Wins" if r == 'O' else "Draw")

