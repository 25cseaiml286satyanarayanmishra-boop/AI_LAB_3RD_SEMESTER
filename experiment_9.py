def print_board(board):
    """Displays the current state of the board."""
    print("\n")
    for i, row in enumerate(board):
        print(" " + " | ".join(row) + " ")
        if i < 2:
            print("---+---+---")
    print("\n")

def check_winner(board):
    """Checks rows, columns, and diagonals for a winner."""
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return True

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True

    return False

def is_board_full(board):
    """Checks if there are any empty spaces left on the board."""
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    """Main function to run the Tic-Tac-Toe game."""
    # Initialize a clean 3x3 board
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    print("Welcome to Tic-Tac-Toe!")
    print("Enter your move by choosing a row (0-2) and a column (0-2) separated by a space.")

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn.")

        # Get and validate user input
        try:
            user_input = input("Enter row and column (e.g., 0 2): ").split()
            if len(user_input) != 2:
                print("Invalid input! Please enter two numbers separated by a space.")
                continue

            row, col = int(user_input[0]), int(user_input[1])

            if row not in range(3) or col not in range(3):
                print("Invalid coordinates! Row and column must be 0, 1, or 2.")
                continue

            if board[row][col] != " ":
                print("That spot is already taken! Try another one.")
                continue

        except ValueError:
            print("Invalid input! Please enter numbers only.")
            continue

        # Place the move
        board[row][col] = current_player

        # Check for a win
        if check_winner(board):
            print_board(board)
            print(f"Congratulations! Player {current_player} wins!")
            break

        # Check for a tie
        if is_board_full(board):
            print_board(board)
            print("It's a tie game!")
            break

        # Switch players
        current_player = "O" if current_player == "X" else "X"

# Start the game
if __name__ == "__main__":
    tic_tac_toe()
