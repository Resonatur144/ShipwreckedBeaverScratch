# Copyright © Anri Amane
# This is the main cipher shift codex used by the script.
beaverScratchCodex = {
    'J': 'I',
    'N': 'M',
    'T': 'S',
    'G': 'H',
    'B': 'A',
    'U': 'V',
    'Q': 'R',
    'M': 'N',
    'H': 'G',
    'P': 'O',
    'C': 'D',
    'K': 'L',
    'D': 'C',
    'S': 'T',
    'V': 'U',
    'L': 'K',
    'E': 'F',
    'F': 'E',
    'A': 'B',
    'O': 'P',
    'X': 'W',
    'W': 'X'
}


# Takes the users input and returns it as a string.
def take_console_input():
    ciphertext = input("Enter BeaverScratch to Decode: ")
    return ciphertext


# Use codex to resolve given cipher string into decoded text. (ENGLISH)
def decode_cipher_text(ciphertext: str):
    decodedText = ""
    for cipherElement in ciphertext:
        if cipherElement in beaverScratchCodex.keys():
            decodedText = decodedText + beaverScratchCodex[cipherElement]
        else:
            decodedText = decodedText + cipherElement

    return decodedText

# Entrypoint of script.
def main():
    # Take user input, decode and return
    cipherText = take_console_input().upper()
    decodedText = decode_cipher_text(cipherText)
    print(decodedText)


# Run main.py if launched in PyCharm.
if __name__ == '__main__':
    main()
