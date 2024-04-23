import random

def play():

  user = input("Choose between rock, paper and scissor. R, P, S: ").upper()
  computer = random.choice(["R", "P", "S"])
  print(f"User choice: {user}, Computer choice: {computer}")
  if user == computer:
    return "It's a tie."
  
  if user == "P" and computer == "R" or user == "S" and computer == "P" or user == "R" and computer == "S":
    return"User Win."
  
  return"Computer Win."
  

print(play())


# user choose between rock paper and scissor
# computer chooses between rock paper and scissor
# we compare for winning statement p>r s>p r>s
# we compare for tie
# or continue