# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


def return_text_from_file(path):
    with open(path) as letter_example:
        return letter_example.read()


letter_text = return_text_from_file("Input/Letters/starting_letter.txt")
names = return_text_from_file("Input/Names/invited_names.txt").split("\n")

for name in names:
    # print(letter_text.replace("[name]", name))
    with open(f"Output/ReadyToSend/letter_to_{name}.txt", "w") as edited_letter:
        edited_letter.write(letter_text.replace("[name]", name))

