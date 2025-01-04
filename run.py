import random


class Board:
    """
    Main board class. Stores the board size, the number of ships,
    the position of the ships and the guesses against that board.
    This class has methods as display board, place ship,
    register shot and end of game.
    """

    def __init__(self, size, num_ships, name):
        self.size = size
        self.num_ships = num_ships
        self.name = name
        self.guesses = []
        self.ships = []
        self.board = [["~" for x in range(size)] for y in range(size)]
        self.score = 0

    def display_board(self, show_ships=False):
        """
        Shows the current board, whether or not it reveals
        the position of the ships.
        """

        # Print column numbers at the top
        show_col = "  " + " ".join(str(col) for col in range(self.size))
        print(show_col)

        for i in range(self.size):
            show_row = self.board[i][:]
            if show_ships:
                for col in range(self.size):
                    if (i, col) in self.ships and show_row[col] == "~":
                        show_row[col] = "@"
            print(f"{i} "+" ".join(show_row))

    def place_ship(self):
        """
        Position ships randomly on the board.
        """
        while len(self.ships) < self.num_ships:
            row = random.randint(0, self.size - 1)
            col = random.randint(0, self.size - 1)
            if (row, col) not in self.ships:
                self.ships.append((row, col))

    def register_shot(self, row, col):
        """
        Register a shot on the board and check whether hit or miss.
        Removes the respective coordinates from the ships list
        when a hit occurs and adds a point to score attribute.
        If not, add these coordinates to the guesses list.
        """
        if (row, col) in self.ships:
            self.board[row][col] = "X"
            self.ships.remove((row, col))
            self.score += 1
            print("Hit a ship!")
            return True
        else:
            self.guesses.append((row, col))
            self.board[row][col] = "O"
            print("Miss")
            return False

    def end_of_game(self):
        """
        Checks if all ships have been destroyed.
        """
        return len(self.ships) == 0


def get_valid_coordinates(size, computer_board):
    """
    Function to validate the coordinates. Only allows coordinates that:
    - Are within the board size.
    - Have not been guessed yet.
    - Are not part of already destroyed ships.
    - Only accepts integer input
    """
    while True:
        try:
            user_row = int(input("Enter an integer number for row:\n"))
            user_col = int(input("Enter an integer number for column:\n"))

            if 0 <= user_row < size and 0 <= user_col < size:
                not_guessed = (
                    (user_row, user_col) not in computer_board.guesses)
                not_hit = (
                    computer_board.board[user_row][user_col] not in ["X", "O"]
                    )
                if not_guessed and not_hit:
                    return user_row, user_col
                else:
                    print("Coordinates already guessed or ship destroyed.")
            else:
                print("Coordinates outside the board size limit. Try again.")

        except ValueError:
            print("Invalid input. Enter integer numbers.")


def computer_turn(user_board, user_name):
    """
    Sets the choice made by the computer.
    """
    while True:
        row = random.randint(0, user_board.size - 1)
        col = random.randint(0, user_board.size - 1)

        not_guessed = (row, col) not in user_board.guesses
        not_hit = user_board.board[row][col] not in ["X", "O"]
        if not_guessed and not_hit:
            print("-" * 34)
            print(f"Computer shoots at ({row},{col})")
            user_board.register_shot(row, col)
            print("-" * 34)
            print(f"{user_name}'s board")
            user_board.display_board(show_ships=True)
            break


def winner(user_board, computer_board):
    """
    Defines who is the winner of the game once it is finish.
    """
    # Check if the player is the winner
    if computer_board.end_of_game():
        print("You destroyed all the computer's ships")
        display_scores(user_board, computer_board)
        return True

    # Check if the computer is the winner
    elif user_board.end_of_game():
        print("Computer destroyed all your ships")
        display_scores(user_board, computer_board)
        return True

    else:
        return False


def still_exit():
    """
    To decide whether the game still continues or whether
    and to exit it.
    """
    while True:
        print("Enter any key to continue or 'e' to exit:")
        still = input().lower()
        if still == "e":
            exit()
        else:
            break


def display_scores(user_board, computer_board):
    """
    Display the scores for both the user and the computer.
    """
    print("-" * 34)
    print(f"Score for {user_board.name}: {computer_board.score}")
    print(f"Score for {computer_board.name}: {user_board.score}")
    print("-" * 34)
    still_exit()


def play_game(user_board, computer_board, user_name):
    """
    Main play game function.
    """
    new_game = Board(size=5, num_ships=4, name="Computer")

    while not winner(user_board, computer_board):
        print("-" * 34)
        print("Your turn!")
        row, col = get_valid_coordinates(computer_board.size, computer_board)
        computer_board.register_shot(row, col)
        print("-" * 34)
        print("Computer's board")
        computer_board.display_board(show_ships=False)

        if winner(user_board, computer_board):
            break
        # Computer's turn
        computer_turn(user_board, user_name)
        if winner(user_board, computer_board):
            break

        # Display scores after computer's turn
        display_scores(user_board, computer_board)


def new_game():
    """
    Starts a new game.
    Initialize user's and computers's board.
    Sets the board size and number of ships.
    """

    new_game = Board(size=5, num_ships=4, name="Computer")
    size_number = new_game.size
    number_of_ships = new_game.num_ships

    print("-" * 34)
    print("Welcome to Battle of Ships Game!")
    print(f"Board Size: {size_number}. Number of ships: {number_of_ships}")
    print("Top left corner is row: 0, col: 0")
    print("-" * 34)

    # Initialize user's board
    user_name = input("What is your name?\n")
    print("-" * 34)
    print(f"{user_name}'s board")
    user_board = Board(size=5, num_ships=4, name=user_name)
    user_board.place_ship()
    user_board.display_board(show_ships=True)

    # Initialize computer's board
    computer_board = Board(size=5, num_ships=4, name="Computer")
    computer_board.place_ship()

    play_game(user_board, computer_board, user_name)


new_game()
