# Treasure Island
print('''
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
                                                                 
''')
print("Welcome to Treasure Island...")
print("Your mission is to find the treasure...")

q1 = input("Whether you want to go left or right? ")
if q1 == 'left':
    print("Game Over!!")
else:
    q2 = input("Whether you wanna wait or swim? ")
    if q2 == 'swim':
        print("Game Over!!")
    else:
        print('''Select a door:
        Red
        Yellow
        Green''')
        q3 = input("Which door? ")
        if q3 == 'Green':
            print("You Won!!")
        else:
            print("Game Over!!")