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

class Board:
   """
   Main board class. Sets board size, the number of ships, the player's name
   This class has methods for display board, place ship, register shot and end of game
   """
   def __init__(self, size, num_ships, name):
      self.size = size
      self.num_ships = num_ships
      self.name = name
      self.guesses = [] # all the guesses that were made against the board
      self.ships = [] # The coordinates of the ships on board
      self.board = [["~" for x in range(size)] for y in range(size)]
      


   def display_board(self, show_ships=False):
      """
      Shows the current board, whether or not it reveals the position of the ships
      """

      #Print column numbers at the top
      show_col = "  "+" ".join(str(col) for col in range(self.size))
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
      Position ships randomly on the board
      """
      while len(self.ships) < self.num_ships:
         row = random.randint(0, self.size-1)
         col = random.randint(0, self.size -1)
         if (row, col) not in self.ships:
            self.ships.append((row, col))

   def register_shot(self, row, col):
      """
      Register a shot on the board and check whether it was right or wrong
      """ 
      #Update the board
      if(row, col) in self.ships:
         self.board[row][col] = "X"
         self.ships.remove((row, col))
         print("Hit a ship!")
         return True
      else:
         #Record the guess
         self.guesses.append((row,col))
         self.board[row][col] = "O"
         print("Wrong")
         return False

 
        
   def end_of_game (self):
      """ 
      Checks if all ships have been destroyed
      """
      return len(self.ships) == 0




def get_valid_coordinates(size, computer_board):
   """
   Function to validate the coordinates
   """
   while True:
      try:
         user_row = int(input("Enter a integer number for row: "))
         user_col = int(input("Enter a integer number for column: "))
         if 0 <= user_row < size and 0 <= user_col < size:
            if (user_row, user_col) not in computer_board.guesses:
               return user_row, user_col
            else:
               print(" You can't use the same coordinates twice.")

         else:
            print("Coordinates outside the board size limit.Please try again.")
      except ValueError:
         print("Invalid input. Enter integers numbers ")
         



def computer_turn(user_board, user_name):
   """
   Sets the computer's move
   """
   
   while True:
      row = random.randint(0, user_board.size - 1)
      col = random.randint(0, user_board.size - 1)
      if (row, col) not in user_board.guesses:
         print(f"Computer shoots at ({row},{col})")
         user_board.register_shot(row, col)
         print(f"{user_name}'s board")
         user_board.display_board(show_ships=True)
         break




def winner (user_board, computer_board):
   """
   Winner of the game
   """
   #Check if the player is the winner
   if computer_board.end_of_game():
      print("You destroyed all the computer ships")
      return True

   #Check if the computer is the winner
   elif user_board.end_of_game():
      print("Computer destroyed all your ships")
      return True

   else:

      return False


def play_game(user_board,computer_board, user_name):
   """
   Main play game function 
   """
     
   new_game=Board(size=5,num_ships=4,name="Computer")
   user_ships=new_game.num_ships
   computer_ships=new_game.num_ships


   while not winner(user_board,computer_board):
      #Player's turn
      print("Your turn!")
      row, col = get_valid_coordinates(computer_board.size, computer_board)
      computer_board.register_shot(row, col)

      print("Computer's board")
      computer_board.display_board(show_ships=True) #After test change this to Fasle

      #Clean this four prints when finish to test
      print(computer_board.guesses)# The list of user's guess
      print(user_board.guesses)# The list of computer's guess
      print(user_board.ships)# The list of user board ships
      print(computer_board.ships)# The list of computer board ships

      if winner(user_board, computer_board):
         break
      #Computer's turn
      computer_turn(user_board, user_name)
      if winner(user_board, computer_board):
         break



def new_game():
   """
   Function to Initialize user's and computers's board
   """
   
   new_game=Board(size=5,num_ships=4,name="Computer")
   size_number=new_game.size
   number_of_ships=new_game.num_ships

   print("Welcome to Battle of Ships Game!")
   print(f"Board Size:{size_number}. Number of ships: {number_of_ships}")
   
   print("Start board")
   new_game.display_board(show_ships=True)
   
   #Initialize user's board
   user_name=input("What is your name? ")
   print(f"{user_name}'s board")
   user_board = Board(size=5,num_ships=4,name="Player")
   user_board.place_ship()
   user_board.display_board(show_ships=True)
   
   
   #Initialize computer's board
   print("computer's board")
   computer_board = Board(size=5,num_ships=4,name="Computer")
   
   computer_board.place_ship()
   computer_board.display_board(show_ships=False)

  
   play_game(user_board,computer_board,user_name)



new_game()