import random
from replit import clear
from art import logo

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)

def calculate_score(list_of_cards):

  if sum(list_of_cards) == 21 and len(list_of_cards) == 2:
    return 0

  if sum(list_of_cards) > 21 and 11 in list_of_cards:
    list_of_cards.remove(11)
    list_of_cards.append(1)
    
  return sum(list_of_cards)

def compare(user_score, computer_score):
  if user_score == computer_score:
    return "Draw"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack"
  elif user_score == 0:
    return "Win with a Blackjack"
  elif user_score > 21:
    return "You went over. You lose"
  elif computer_score > 21:
    return "Opponent went over. You win"
  elif user_score > computer_score:
    return "You win"
  else:
    return "You lose"

def play_game():

  print(logo)

  user_cards = []
  computer_cards = []
  game_over = False

  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  
  while not game_over:
    
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"   Your hand: {user_cards}, current score: {user_score}")
    print(f"   Computer's first card: {computer_cards[0]}")


    if computer_score == 0 or user_score == 0 or user_score > 21:
      game_over = True
    else:
      
      user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
      if user_should_deal == 'y':
        user_cards.append(deal_card())
      else:
        game_over = True
      

  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"   Your final hand: {user_cards}, final score: {user_score}")
  print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))


while input("Do want to play a game of Blackjac? Type 'y' or 'n': ") == 'y':
  clear()
  play_game()