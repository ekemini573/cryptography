
#The string to be encrypted/decrypted:
message = 'This is my secret message'

#The encrytion/decryption key:
key = 13

#Whether the program encrypts or decrypts
mode = 'encrypt'

#Every possible symbol that can be encrypted
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'

#Store the encrypted/decrypted form of the message
translated = ' '

for symbol in message:
    #NOTE: only symbols in the SYMBOLS string can be encrypted/decrypted.
    if symbol in SYMBOLS:
        #gets the index of SYMBOLS
        symbolsIndex = SYMBOLS.find(symbol)

        #performs decryption/encryption
        if mode == 'encrypt':
            translatedIndex = symbolsIndex + key

        elif mode == 'decrypt':
            translatedIndex = symbolsIndex - key

        # Handle wraparound, if needed
        if translatedIndex >= len(SYMBOLS):
             translatedIndex = translatedIndex - len(SYMBOLS)
        elif translatedIndex < 0:
            translatedIndex = translatedIndex + len(SYMBOLS)

        translated = translated + SYMBOLS[translatedIndex]

    else:
        # Append the symbol without encrypting/decrypting:
        translated = translated + symbol

#Output the translated string
print(translated)

