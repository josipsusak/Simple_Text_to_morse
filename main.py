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
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}

service = input("Please choose what do you wanna do? Encrypt or decrypt: ").lower()
text = input("Please insert your text: ").upper()


# Function to encrypt user entered text
def encrypt(message):
    encrypted_text = ""
    for letter in message:
        # Checks the message entered and if it's not a space,
        # looks up the corresponding morse code in dictionary,
        # and adds a space at the end to separate different characters
        if letter != " ":
            encrypted_text += MORSE_CODE_DICT[letter] + " "
        else:
            encrypted_text += " "
    print(encrypted_text)


def decrypt(message):
    decrypted_text = ""
    characters = ""
    # Adds space to the end of message to get access to last letter
    message += " "
    # new dictionary made from first one to reverse search for letters
    swapped_dictionary = {morse: letter for letter, morse in MORSE_CODE_DICT.items()}

    for letter in message:
        if letter != " ":
            # Counter to check for spaces, one space is new character, two spaces is new word
            spaces = 0
            # Storing morse code of a single character
            characters += letter
        else:
            spaces += 1
            # If there is a new word, we add space to the text
            if spaces == 2:
                decrypted_text += " "
            else:
                # Search through the reversed dictionary and replace with letter/word
                decrypted_text += swapped_dictionary[characters]
                characters = ""
    print(decrypted_text)


if service == "encrypt":
    encrypt(text)

else:
    decrypt(text)
