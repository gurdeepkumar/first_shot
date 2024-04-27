import random
from itertools import islice
from player import RandomComputerPlayer, HumanPlayer

class TicTacToe:
  #initializing the variables
  def __init__(self):
    self.board = [" " for i in range(9)]
    self.current_winner = None
    self.updatedboard = []

  def print_board_structure(self):
    self.updated_board = [str(index) for index,val in enumerate(self.board)]
    for i in range(3):
      row = [spot for spot in self.updated_board[i*3:i*3+3]]
      print("|".join(row))

  def print_board(self):
    self.updated_board = [val for index,val in enumerate(self.board)]
    for i in range(3):
      row = [spot for spot in self.updated_board[i*3:i*3+3]]
      print("|".join(row))

  def empty_cells(self):
    return self.board.count(" ")

  def available_moves(self):
    return [i for i, spot in enumerate(self.board) if spot  == " "]
  
  def make_move(self, move, letter):
    if self.board[move] == " ":
      self.board[move] = letter
      if self.check_winner(move, letter):
        self.current_winner = letter
      return True
    return False
    
  def check_winner(self, move, letter):

    row_index = move // 3
    row = self.board[row_index*3:row_index*3+3]
    if (all(spot == letter for spot in row)):
      return True
    
    col_index = move % 3
    col = list(islice(self.board,col_index,9,3))
    if all(spot == letter for spot in col):
      return True
    
    if move % 2 == 0:
      diagnol1 = [self.board[i] for i in [0, 4, 8]]
      if all(spot == letter for spot in diagnol1):
        return True
      diagnol2 = [self.board[i] for i in [2, 4, 6]]
      if all(spot == letter for spot in diagnol2):
        return True
      
    return False


def play(game, x_player, o_player, print_game = True):
  if print_game:
    game.print_board_structure()
  letter = "X" # starting letter 
  while game.empty_cells() != 0:
    if letter == "O":
      move = o_player.get_move(game)
    else:
      move = x_player.get_move(game)
    
    if game.make_move(move, letter):
      if print_game:
        print(f"{letter} makes a move to spot {move}")
        game.print_board()
        print(" ")
      
      if game.current_winner:
        if print_game:
          print(f"{letter} wins!")
        return letter
      
      if letter == "O":
        letter = "X"
      else:
        letter = "O"
  if print_game:
    print("It's a tie.")

if __name__ == "__main__":
  x_player = HumanPlayer("X")
  o_player = RandomComputerPlayer("O")
  t = TicTacToe()
  play(t, x_player, o_player, print_game=True)