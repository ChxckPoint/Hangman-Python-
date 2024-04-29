
import time
import os
import random
import sys
import time
import pyfiglet
from colorama import init
from pyfiglet import figlet_format
from termcolor import colored

#Title of game
init(autoreset=False, convert=None, strip=None, wrap=True)
print((colored(figlet_format("Welcome to Hangman !\n"), color = 'green')))

#slow print allows for dialog to print at a specified speed
def print_slow_1(str):
  for letter in str:
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(0.04)

#day 2 gretting user input and rules 
print_slow_1("what is your name? ")
name = input("")
print_slow_1("\nHello, " + name + " welcome to hangman, are you familiar with the rules of the game? ")
rules = input("")

if rules == "yes" or rules == "Yes":
  os.system("clear")
  print_slow_1("\nOkay, LETS PLAY!\n\n")

elif rules =="no" or rules == "No":
  print_slow_1("\nYou will be prompted to guess a word but only ONE letter at a time, if you figured out the word you MUST only guess one letter at a time. Good luck.\n")
  time.sleep(3)
  os.system("clear")

#global parameters, list of words, and picks random word
def body():# day 3
  global game, blanks, count, pick_word, alr_guessed, length_ow
  count = 0
  words = ["fox", "cow", "cat", "mouse", "stop", "moose", "June", "dark","threat", "bat", "throw", "credit", "raise", "bed", "reach", "normal", "wheel", "chaos", "gain", "fish", "joke", "hangman", "skilled", "teach", "word", "wire", "false", "lot", "shock", "mars" ]
  
  pick_word = random.choice(words)
  alr_guessed = []
  length_ow = len(pick_word)
  blanks = "_"*length_ow
  game = ""


#loop to re-play game once finished
def play():
  global game
  game = input("\nYou want to play again or you just a chicken? (yes or no) ")
  
  if game == "yes" or game =="Yes":
    os.system("clear")
    body()
  elif game == "no":
    print_slow_1("\nThats lame, come play some other time..")
    exit()

#asks for user input for guess and will determine if its in the word and if it should print the structure
def man():# day 4
  global game, blanks, count, pick_word, alr_guessed
  max_guesses = 7
  guess = input("This is the word " + blanks + " \n\nEnter a letter: ")
  guess.lower()
  guess = guess.strip()
  if len(guess.strip())== 0 or len(guess.strip()) > 1 or guess <= "9":
    print_slow_1("Your supposed to guess ONE letter and NO numbers. try again\n")
    man()
    
  elif guess in pick_word:
    alr_guessed.extend([guess])
    i = pick_word.find(guess)
    pick_word = pick_word[:i] + "_" + pick_word[i + 1:]
    blanks = blanks[:i] + guess + blanks[i + 1:]
    print(blanks + "\n")
    
  elif guess in alr_guessed: #day 5
    print("You already guessed that one. You have short term memory loss or somthin'?\n\n")
    
  else:
    count +=1
#hangman structure
    if count == 1:
      print("________      ")
      print("|      |      ")
      print("|             ")
      print("|             ")
      print("|             ")
      print("|             ")
      print("_________")
      print("\nWrong! "+ str(max_guesses - count) + " guesses left\n")

    elif count == 2:
      print("________      ")
      print("|      |      ")
      print("|      0      ")
      print("|             ")
      print("|             ")
      print("|             ")
      print("_________")
      print("\nWrong! "+ str(max_guesses - count) + " guesses left\n")

    elif count == 3:
      print("________      ")
      print("|      |      ")
      print("|      0      ")
      print("|     /      ")
      print("|             ")
      print("|             ")
      print("_________")
      print("\nWrong! "+ str(max_guesses - count) + " guesses left\n")

    elif count == 4:
      print("________      ")
      print("|      |      ")
      print("|      0      ")
      print("|     /|       ")
      print("|             ")
      print("|             ")
      print("_________")
      print("\nWrong! "+ str(max_guesses - count) + " guesses left\n")



    elif count == 5:
      print("________      ")
      print("|      |      ")
      print("|      0      ")
      print("|     /|\       ")
      print("|             ")
      print("|             ")
      print("_________")
      print("\nWrong! "+ str(max_guesses - count) + " guesses left\n")


    elif count == 6:
      print("________      ")
      print("|      |      ")
      print("|      0      ")
      print("|     /|\      ")
      print("|     /       ")
      print("|             ")
      print("_________")
      print("\nWrong! "+ str(max_guesses - count) + " guesses left\n")

    elif count == 7:#after 7 guesses user is taken to the lose route
      print("________      ")
      print("|      |      ")
      print("|      0      ")
      print("|     /|\      ")
      print("|     / \      ")
      print("|             ")
      print("_________")
      print("\nWrong! You lost.")
      print("\nThe word was: ",pick_word,alr_guessed)
      play()
      
#win route if the word is guessed
  if pick_word == "_"*length_ow:
    print_slow_1("WOW you got it! Good Job! " + name)
    play()

  elif count != max_guesses:
    man()
        
body()
man()