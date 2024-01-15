import art

print(art.logo)

def caeser(choice, text, shift):
    new_text = ""
    for letter in text:
        if letter in alphabets:
            position = alphabets.index(letter)
            if choice == 'Encrypt':
                new_text += alphabets[position + shift]
            elif choice == 'Decrypt':
                new_text += alphabets[position - shift]
        else:
            new_text += letter

    print(f"{choice}ed text is: {new_text}")

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
repeat = ''
while repeat != 'n':
    choice = input("Encrypt or Decrypt: ").capitalize()
    text = input(f"Enter text to {choice}: ").lower()
    shift = int(input("Enter number of shift: "))
    shift %= 26
    caeser(choice, text, shift)
    repeat = input("Type 'y' for continue or 'n' for exit: ")
