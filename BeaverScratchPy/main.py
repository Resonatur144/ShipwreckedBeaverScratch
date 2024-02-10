# I wrote this to easily decode BeaverScratch for myself for the game Shipwrecked64.
# I don't recommend the approach I took here for how to code "WELL-MADE" shift cipher decoders.
# Most basic ciphers use modulus in some respect, however it seemed like BeaverScratch was different
# as my approaches didn't work, so I brute forced the codex you see below.

# Obviously there are way better ways to code this, and I simply hard coded the codex to just have a quick tool.
# But hopefully for those wishing to understand more about cryptography this gives you insight.

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
