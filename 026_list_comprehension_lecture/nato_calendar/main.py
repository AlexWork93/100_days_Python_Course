import pandas

nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")

dict_nato = {row.letter: row.code for (index, row) in nato_df.iterrows()}
keep_ask = True
user_input_in_nato = []
while keep_ask:
    user_input = input("what should I convert to NATO alphabet?: ")
    try:
        user_input_in_nato = [dict_nato[n] for n in user_input.upper() if not n == ' ']
    except KeyError:
        print("Only letters are allowed!")
    else:
        keep_ask = False

print(user_input_in_nato)

# TODO 1. Create a dictionary in this format:

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
