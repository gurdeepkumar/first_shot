import random


class Player:
  def __init__(self, letter):
    #letter is X or O
    self.letter = letter
  def get_move(self, game):
    pass

class RandomComputerPlayer(Player):
  def __init__(self, letter):
    super().__init__(letter)
  def get_move(self, TicTacToe):
    computer_move = int(random.choice(TicTacToe.available_moves()))
    return computer_move 

class HumanPlayer(Player):
  def __init__(self, letter):
    super().__init__(letter)
  def get_move(self, TicTacToe):
    valid_move = False
    val = None
    while not valid_move:
      user_move = input(f"{self.letter}'s turn. Enter move (0-8): ")
      try:
        val = int(user_move)
        if val not in TicTacToe.available_moves():
          raise ValueError
        valid_move = True
      except:
        print("Invalid move. Try again. ")
    return val