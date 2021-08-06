all_symbols = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    " ": " ",
}

while True:

    user_input = input("Type here,  what you want to translate to morse code: ").upper()

    print("Here is your output in morse code: ")

    for letter in user_input:
        try:
            if letter == " ":
                print("")
            else:
                print(letter, " = ",  all_symbols[letter])

        except KeyError:
            print(f"This symbol '{letter}' is not supported by this morse code")

    user_continue = input("Do you want to continue ? Type 'Y' or 'N' ").upper()
    if user_continue != "Y":
        break
