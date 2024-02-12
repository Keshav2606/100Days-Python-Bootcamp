import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")

data_dict = {row.letter: row.code for (index, row) in df.iterrows()}

user_input = input("Enter a word: ")

list_of_phonetic_words = [data_dict[char.upper()] for char in user_input]

print(list_of_phonetic_words)
