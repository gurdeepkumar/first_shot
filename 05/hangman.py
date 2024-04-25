import random
import string

from words import words

def get_valid_word(words):
  guess = random.choice(words)
  while "-" in guess or " " in guess:
    guess = random.choice(words)
  return guess.upper()

def hangman(lives):

  word = get_valid_word(words)
  print(word)
  letters_in_word = set(word)
  alphabets = set(string.ascii_uppercase)
  used_letter = set()

  while len(letters_in_word) > 0 and lives > 0:

    print(f"You have {lives} left.")
    word_list = [letter if letter in used_letter else "-" for letter in word]
    print("The word: ", " ".join(word_list))
    print("Used letters: ", " ".join(used_letter))  

    user_input = input("Guess a letter: ").upper()
    if user_input in alphabets - used_letter:
      used_letter.add(user_input)
      if user_input in letters_in_word:
        letters_in_word.remove(user_input)
      else:
        lives = lives - 1
    
    elif user_input in used_letter:
      print("You already used this letter. Try again !")
    
    else:
      print("Invalid Character!")
  
  if lives == 0:
    print(f"You lost. The word was: {word}")
  else:
    print(f"You won. You guseed the word: {word}")


      
  

hangman(10)