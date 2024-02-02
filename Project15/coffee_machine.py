from resources import MENU, resources

def report():
    global profit

    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"Money: ₹{profit}")


def process_coins():
    global profit
    to_pay = MENU[user_input]["cost"]
    print(f"You Ordered {user_input}. Pay: ₹{to_pay} in change. ")
    print("Please insert Money.")
    curr10 = int(input("How much ₹10 Note: "))
    curr20 = int(input("How much ₹20 Note: "))
    curr50 = int(input("How much ₹50 Note: "))
    curr100 = int(input("How much ₹100 Note: "))
    amount = (10 * curr10) + (20 * curr20) + (50 * curr50) + (100 * curr100)

    if amount >= to_pay:
        change = amount - to_pay
        print(f"Here is ₹{change} in change.")
        profit += to_pay
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False

def check_resources():
    if MENU[user_input]["ingredients"]["water"] > resources["water"]:
        print("Sorry, there is not enough water.")
        return False
    elif MENU[user_input]["ingredients"]["milk"] > resources["milk"]:
        print("Sorry, there is not enough milk.")
        return False
    elif MENU[user_input]["ingredients"]["coffee"] > resources["coffee"]:
        print("Sorry, there is not enough coffee.")
        return False
    else:
        return True
    
def update_resources(user_input):
    resources["water"] -= MENU[user_input]["ingredients"]["water"]
    resources["milk"] -= MENU[user_input]["ingredients"]["milk"]
    resources["coffee"] -= MENU[user_input]["ingredients"]["coffee"]

profit = 0
is_on = True
while is_on:
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_input == 'report':
        report()
    elif user_input == 'off':
        is_on = False
    else:
        if check_resources():
            if process_coins():
                print(f"Here is your {user_input} ☕ enjoy!!")
                update_resources(user_input)