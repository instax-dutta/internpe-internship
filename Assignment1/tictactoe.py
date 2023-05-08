def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def check_winner(board):
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] and board[i] != "-":
            return board[i]

    for i in range(3):
        if board[i] == board[i+3] == board[i+6] and board[i] != "-":
            return board[i]

    if board[0] == board[4] == board[8] and board[0] != "-":
        return board[0]
    if board[2] == board[4] == board[6] and board[2] != "-":
        return board[2]

    if "-" not in board:
        return "Tie"

    return None

def play_game():
    board = ["-", "-", "-",
             "-", "-", "-",
             "-", "-", "-"]
    current_player = "X"
    winner = None

    print_board(board)

    while not winner:
        move = int(input(f"Player {current_player}, enter a position (1-9): ")) - 1

        if board[move] != "-":
            print("Invalid move. Try again.")
            continue

        board[move] = current_player

        winner = check_winner(board)

        current_player = "O" if current_player == "X" else "X"

        print_board(board)

    if winner == "Tie":
        print("It's a tie!")
    else:
        print(f"Player {winner} wins!")

play_game()
