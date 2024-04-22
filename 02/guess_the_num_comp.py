import random

def guess(x):
  random_num = random.randint(1,x)
  
  guess = 0

  while (guess != random_num):
    guess = int(input(f"Guess a number between 1 and {x}: "))
    
    if guess <  random_num:
      print("The guess is too low.")
    elif guess > random_num:
      print("The num is too high.")
  
  print(f"You Gussed the random number. It is {random_num}")

guess(10)