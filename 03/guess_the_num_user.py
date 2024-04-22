import random

def computer_guess(x):
  input("Have a secret num from 1 to 10. Press any key after having number to contiue the game.")
  feedback = " "
  y = 1
  guess = " "
  while feedback != "X":
    if x != y:
      guess = random.randint(y,x)
    else:
      guess = x
      
    print(f"Is the number {guess} ?")

    feedback = input("Press L, if number is too low. Press H, if number is too high. Press X, if i gussed the number: ").upper()

    if feedback == "L":
      y = guess + 1
    elif feedback == "H":
      x = guess - 1

  print(f"Computer gussed the number and it is {guess}.")




# computer asks us to guess number between a range 1 to 10.   
# computer guesses the number from range 
# we input if num is too high or too low
# if num is too high compter make that range high
# if the num is too low computer make that range low 
# or it guessed the right number

computer_guess(10)