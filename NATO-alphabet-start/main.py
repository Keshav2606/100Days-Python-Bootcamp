import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")

data_dict = {row.letter: row.code for (index, row) in df.iterrows()}


def generate_phonetic():
    user_input = input("Enter a word: ")

    try:
        list_of_phonetic_words = [data_dict[char.upper()] for char in user_input]
    except KeyError:
        print("Sorry, Only alphabets in the letter.")
        generate_phonetic()
    else:
        print(list_of_phonetic_words)


generate_phonetic()
