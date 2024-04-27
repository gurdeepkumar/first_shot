import random
from itertools import islice

def print_board(board):
  updated_board = [val if val != " " else str(index) for index,val in enumerate(board)]
  for i in range(3):
    row = [spot for spot in updated_board[i*3:i*3+3]]
    print("|".join(row))

def empty_cells(board):
  return board.count(" ")

def avaiable_spots(board):
  return [i for i, j in enumerate(board) if j == " "]

def check_winner(board):
  for i in range(3):
    if (all(spot == "X" for spot in board[i*3:i*3+3])):
      return "X wins"
    elif (all(spot == "O" for spot in board[i*3:i*3+3])):
      return "O wins"
    elif (all(spot == "X" for spot in islice(board,i,9,3))):
      return "X wins"
    elif (all(spot == "O" for spot in islice(board,i,9,3))):
      return "O wins"
    
  if (all(spot == "X" for spot in islice(board,0,9,4))) or (all(spot == "X" for spot in islice(board,2,8,2))):
    return "X wins"
  elif (all(spot == "O" for spot in islice(board,0,9,4))) or (all(spot == "O" for spot in islice(board,2,8,2))):
    return "O wins"

def game_tictactoe():
  board = [" " for i in range(9)]

  user_sign = input("What sign you want ? X or O :").upper()
  if user_sign == "X":
    computer_sign = "O"
  else:
    computer_sign = "X"

  while empty_cells(board) != 0: 
    print_board(board)
    avaiable_moves = avaiable_spots(board)    
    
    user_move = int(input("Input your move: (0-8): "))
    while user_move not in avaiable_moves:
      user_move = int(input("Move not avaialable. Try again: (0-8): "))
    board[user_move] = user_sign

    if check_winner(board) == "X wins":
      print(f"***** X Wins *****")
      print_board(board)
      break
    elif check_winner(board) == "O wins":
      print(f"***** O Wins *****")
      print_board(board)
      break

    if empty_cells(board) != 0:
      print_board(board)
      avaiable_moves = avaiable_spots(board)
      computer_move = int(random.choice(avaiable_moves))
      print(f"Computer's move is: {computer_move}")
      board[computer_move]=computer_sign
      if check_winner(board) == "X wins":
        print(f"***** X Wins *****")
        print_board(board)
        break
      elif check_winner(board) == "O wins":
        print(f"***** O Wins *****")
        print_board(board)
        break
  
  #empty_cells loop finsihes here:
  print("The end.")

game_tictactoe()