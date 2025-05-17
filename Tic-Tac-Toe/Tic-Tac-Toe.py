import random

board = [
    ["1", "2", "3"],
    ["4", "X", "6"],
    ["7", "8", "9"]
]
current_player = "O"
game_is_running = True
winner = None

def board_display(board):
    print("+-------+-------+-------+")
    for row in board:
        print("|       |       |       |")
        print(f"|   {row[0]}   |   {row[1]}   |   {row[2]}   |")
        print("|       |       |       |")
        print("+-------+-------+-------+")

def enter_move():
    global current_player
    while True:
        try:
            move = int(input("Please Enter A Number From 1 To 9: "))
            row = (move - 1) // 3
            col = (move - 1) % 3
            if move >= 1 and move <= 9 and board[row][col].isdigit():
                board[row][col] = current_player
                break
            else:
                print("Invalid Move or Position Occupied. Try again.")
        except ValueError:
            print("Invalid Input. Please Enter A Number Between 1 And 9.")

def make_list_of_free_fields(board):
    free_fields = []
    for i in range(3):
        for j in range(3):
            if board[i][j] != "X" and board[i][j] != "O":
                free_fields.append((i,j))
    return free_fields

def random_move():
    free_field = make_list_of_free_fields(board)
    if free_field:
        row, col = random.choice(free_field)
        board[row][col] = "X"
        print("----------------------------------")
        print("Computer Placed An X On The Board!")

def check_winner(board):
    global winner, game_is_running
    for n in range(3):
        if board[n][0] == board[n][1] == board[n][2]:
            winner = board[n][0]
            game_is_running = False
            return
        if board[0][n] == board[1][n] == board[2][n]:
            winner = board[0][n]
            game_is_running = False
            return
    if board[0][0] == board[1][1] == board[2][2]:
        winner = board[0][0]
        game_is_running = False
        return
    if board[0][2] == board[1][1] == board[2][0]:
        winner = board[0][2]
        game_is_running = False
        return

def draw_move():
    global game_is_running
    if len(make_list_of_free_fields(board)) == 0 and not check_winner(board):
        print("It's A Draw!")
        return True
    return False


while game_is_running:
    board_display(board)
    enter_move()
    check_winner(board)
    if not game_is_running:
        break
    if draw_move():
        break
    random_move()
    check_winner(board)
    if not game_is_running:
        break
    if draw_move():
        break

board_display(board)

if winner:
    print(f"Player {winner} Wins!")
else:
    print("It's A Draw")
