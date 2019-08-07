def encode_caesar_cipher():
    print("Enter your secret message below.")
    caesar_message = input("Message: ")
    print("Now enter a key to shift by.")
    caesar_key = int(input("Key: "))
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    partialOne = ""
    partialTwo = ""
    newAlphabet = ""
    if caesar_key == 0:
        newAlphabet = alphabet
    elif caesar_key > 0:
        partialOne = alphabet[:caesar_key]
        partialTwo = alphabet[caesar_key:]
        newAlphabet = partialTwo + partialOne
    else:
        partialOne = alphabet[:(26 + caesar_key)]
        partialTwo = alphabet[(26 + caesar_key):]
        newAlphabet = partialTwo + partialOne
    newMessage = ""
    for i in range(0, len(caesar_message)):
        index = alphabet.find(caesar_message[i])
        if index < 0:
            newMessage += caesar_message[i]
        else:
            newMessage += newAlphabet[index]
    print("Your Encoded Message: " + newMessage)
