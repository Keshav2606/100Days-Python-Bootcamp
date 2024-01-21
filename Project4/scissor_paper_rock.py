# Rock, Paper, Scissor Game

paper = '''
     _.-._
    | | | |_
    | | | | |
    | | | | |
  _ |  '-._ |
  \`\`-.'-._;
   \    '   |
    \  .`  /
     |    |

'''

rock = '''
      _____
   /\| | | |
  / /|_|_|_|
  \        |
   \_______/
   /______/
'''

scissor = '''
  _       ,/'
   (_).  ,/'
   __  ::
  (__)'  `\.
            `\.
'''
import random

options = [rock, paper, scissor]
print("What you want to choose?")
print('''
1. Rock
2. Paper
3. Scissor
''')

user_choice = int(input())-1
print("Your Choice is:\n",options[user_choice])
computer_choice = random.randint(0,2)
print("Computer chosed:\n",options[computer_choice])

if user_choice == computer_choice:
    print("Match Drawn!!")
elif user_choice == 0 and computer_choice == 1:
    print("You Loosed!!")
elif user_choice == 0 and computer_choice == 2:
    print("You Won!!")
elif user_choice == 1 and computer_choice == 0:
    print("You Won!!")
elif user_choice == 1 and computer_choice == 2:
    print("You Loosed!!")
elif user_choice == 2 and computer_choice == 0:
    print("You Loosed!!")
elif user_choice == 2 and computer_choice == 1:
    print("You Won!!")



