import random
import os
from art import logo


def getRandomCard():
  '''Return a random card from the deck.'''
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(cards):
  score = sum(cards)
  if score == 21 and len(cards) == 2:
    return 0
  if score > 21 and 11 in cards:
    cards.remove(11)
    cards.append(1)
  
  return score

def compare(user_score, computer_score):
  if user_score == computer_score:
    print("Drawn!!")
  elif user_score == 0:
    print("You Won with a BlackJack!!")
  elif computer_score == 0:
    print("You Lose, Opponent has a BlackJack!!")
  elif user_score > 21:
    print("You went Over, You Lose!!")
  elif computer_score > 21:
    print("Opponent went Over, You Won!!")
  elif user_score > computer_score:
    print("You won!!")
  else:
    print("You Lose!!")

restart = ""
print(logo)
while restart != 'n':
  user_cards = [getRandomCard(), getRandomCard()]
  computer_cards = [getRandomCard(), getRandomCard()]
  
  isGameOver = False
  while not isGameOver:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your Cards = {user_cards}, current score = {user_score}")
    print(f"Computer's first Card is: {computer_cards[0]}")
    if user_score == 0 or computer_score == 0 or user_score > 21:
      isGameOver = True
    else:
      ask = input("Do you want to draw new card? ")
      if ask == 'y':
        user_cards.append(getRandomCard())
      elif ask == 'n':
        isGameOver = True
        
    while computer_score < 17 and computer_score != 0:
        computer_cards.append(getRandomCard())
        computer_score = calculate_score(computer_cards)
  print(f"Your final hand: {user_cards}, final score: {user_score}")
  print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
  compare(user_score, computer_score)
  restart = input("Do you want to play again? ")
  if restart == 'y':
    os.system('cls')
    print(logo)