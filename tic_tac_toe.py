# ==========================================
# Tic-Tac-Toe with Simple AI
# ==========================================

# Create an empty board
board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]


# All possible winning combinations
winning_combinations = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6)
]


# ==========================================
# Display the board
# ==========================================
def display_board():

    print()

    print(" " + board[0] + " | " + board[1] + " | " + board[2])

    print("---+---+---")

    print(" " + board[3] + " | " + board[4] + " | " + board[5])

    print("---+---+---")

    print(" " + board[6] + " | " + board[7] + " | " + board[8])

    print()


# ==========================================
# Check if a player has won
# ==========================================
def check_winner(player):

    for combination in winning_combinations:

        a, b, c = combination

        if board[a] == player and board[b] == player and board[c] == player:

            return True

    return False


# ==========================================
# Check for a draw
# ==========================================
def check_draw():

    return " " not in board


# ==========================================
# Player's move
# ==========================================
def player_move():

    while True:

        try:

            position = int(input("Enter your position (1-9): "))

            # Convert to Python index
            position = position - 1

            # Check valid position
            if position < 0 or position > 8:

                print("Please choose a number from 1 to 9.")

            # Check occupied position
            elif board[position] != " ":

                print("That position is already occupied.")

            else:

                # Put X on the board
                board[position] = "X"

                break

        except ValueError:

            print("Please enter a valid number.")


# ==========================================
# Computer's simple AI
# ==========================================
def computer_move():

    print("Computer is thinking...")

    # Rule 1:
    # Try to win.
    for position in range(9):

        if board[position] == " ":

            board[position] = "O"

            if check_winner("O"):

                print("Computer chose position", position + 1)

                return

            board[position] = " "

    # Rule 2:
    # Block the player from winning.
    for position in range(9):

        if board[position] == " ":

            board[position] = "X"

            if check_winner("X"):

                board[position] = "O"

                print("Computer chose position", position + 1)

                return

            board[position] = " "

    # Rule 3:
    # Choose the center.
    if board[4] == " ":

        board[4] = "O"

        print("Computer chose position 5")

        return

    # Rule 4:
    # Choose a corner.
    corners = [0, 2, 6, 8]

    for position in corners:

        if board[position] == " ":

            board[position] = "O"

            print("Computer chose position", position + 1)

            return

    # Rule 5:
    # Choose any remaining space.
    for position in range(9):

        if board[position] == " ":

            board[position] = "O"

            print("Computer chose position", position + 1)

            return


# ==========================================
# Main game
# ==========================================
def play_game():

    print("===================================")
    print("       TIC-TAC-TOE WITH AI")
    print("===================================")

    print("You are X")
    print("Computer is O")
    print("Choose positions from 1 to 9.")

    while True:

        # Display the board
        display_board()

        # Player's turn
        player_move()

        # Display board after player move
        display_board()

        # Check if player won
        if check_winner("X"):

            print("Congratulations! You won!")

            break

        # Check for draw
        if check_draw():

            print("It's a draw!")

            break

        # Computer's turn
        computer_move()

        # Display board after computer move
        display_board()

        # Check if computer won
        if check_winner("O"):

            print("Computer wins! Better luck next time.")

            break

        # Check for draw
        if check_draw():

            print("It's a draw!")

            break


# Start the game
play_game()