import random
import art
import os
from game_data import data

def get_random_account(data):
    '''Select Random Account from the data'''
    return random.choice(data)

def format_account(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}."


def game():
    account1 = get_random_account(data)
    should_continue = True
    score = 0
    while should_continue:
        print(art.logo)
        if score > 0:
            print(f"You're right! Current Score: {score}")
        print(f"Compare A: {format_account(account1)}")
        print(art.vs)
        account2 = get_random_account(data)
        print(f"Against B: {format_account(account2)}")
        user_input = input("Who has more followers? Type 'A' or 'B': ").upper()
        if user_input == 'A':
            if account1["follower_count"] > account2["follower_count"]:
                score += 1
                os.system('cls')
            else:
                os.system('cls')
                print(art.logo)
                print(f"Sorry, that's wrong. Final Score: {score}")
                should_continue = False
        elif user_input == 'B':
            if account1["follower_count"] < account2["follower_count"]:
                score += 1
                account1 = account2
                os.system('cls')
            else:
                os.system('cls')
                print(art.logo)
                print(f"Sorry, that's wrong. Final Score: {score}")
                should_continue = False

game()

