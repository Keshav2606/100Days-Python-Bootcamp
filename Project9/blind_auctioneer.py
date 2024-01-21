import logo
import os

def welcome_screen():
    print(logo.logo)
    print("Welcome to the Secret Auction Program.")
    print("")


bidders = {}
repeat = ""
while repeat != 'n':
    welcome_screen()
    name = input("What is your Name? ")
    bid_amt = int(input("Enter your bid amount: ₹"))
    bidders[name] = bid_amt
    repeat = input("Is their any other bidder? 'y' for yes or 'n' for no: ").lower()
    if repeat == 'y':
        os.system('cls')
    

highest_bid_amt = 0
winner_name = ""
for bidder in bidders:
    if bidders[bidder] > highest_bid_amt:
        highest_bid_amt = bidders[bidder]
        winner_name = bidder.capitalize()

print(f"\nThe winner is {winner_name} with bid amount of ₹{highest_bid_amt}.")

