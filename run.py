import random


#Initialization
"""
- user vs computer
- create two boards one for each player
- place ships for both players randomly

"""

#Game loop
""" 
-show current player's board
- ask for coordinates
- check if coordinates are valid
- check if hit or miss
   - hit add one value to that player
   - miss no add nothing 
- update board with each move
-switch to next player
"""

#End of game
"""
check if all of player's ships have been destroyed
declare winner

"""


def create_board():
   """
   Create a board 5x5
   """
   board = []
   for i in range(5):
       line = []
       for j in range(5):
         line.append("~")
       board.append(line)
   return board
   

def display_board(board):
   for k in board:
      print(" ".join(k))


def place_ship(board):
   """
   Position four ships randomly on the board
   """

   ships_placed = 0
   num_ships=4

   while ships_placed < num_ships:
      ship_row = random.randint(0,4)
      ship_col = random.randint(0,4)

      #Check if position is empty
      if board[ship_row][ship_col] == "~":
         board[ship_row][ship_col] = "@"
         ships_placed +=1
         #print(f"Ship placed in: row {ship_row}, column {ship_col}")

def user_player():
   name=input("What is your name? ")
   board=create_board()
   place_ship(board)
   print(f"{name}'s board")
   display_board(board)

def computer_player():
   print("computer's board")


def main():
   print("Welcome to Battle of Ships Game!")
   print("Board Size:5. Number of ships: 4")
   board=create_board()
   display_board(board)
   user_player()
   computer_player()
   

main()