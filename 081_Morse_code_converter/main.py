# You will use what you've learnt to create a text-based (command line) program that takes any String input and
# converts it into Morse Code.
#
# You've created plenty of text-based programs in Days 1 -10, so look back at some of those projects if you don't
# remember what a text-base program looks like.
#
# Wikipedia Entry for Morse Code
#
# The design, functionality, code style is all up to you. You're wearing the big-girl/big-boy pants now. So you get
# to decide.
#
# Questions for this assignment
# Reflection Time:
#
# This is a place to journal your experience of completing this project. This will help you figure out how to improve
# as a developer.
#
# Write down how you approached the project. What was hard, what was easy. How might you improve for the next
# project? What was your biggest learning from today? What would you do differently if you were to tackle this
# project again?


MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ',': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}

user_input = input("Pass here a string to convert to morse code:\n")


def convert_to_morse(letter):
    try:
        return MORSE_CODE_DICT[letter.upper()] + ' '
    except KeyError:
        print(f'[ {letter} ] is not supported')
        return ''


strint_to_list_of_morse = [convert_to_morse(n) for n in user_input]

result = ''.join(strint_to_list_of_morse)

print(result)

# Example of output:
# sdfasdf sdfasdf .fsadfas> fsdafas, fasdf
# [   ] is not supported
# [   ] is not supported
# [ > ] is not supported
# [   ] is not supported
# [   ] is not supported
# ... -.. ..-. .- ... -.. ..-. ... -.. ..-. .- ... -.. ..-. .-.-.- ..-. ... .- -.. ..-. .- ... ..-. ... -.. .- ..-. .- ... --..-- ..-. .- ... -.. ..-.