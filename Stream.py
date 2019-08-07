def encode_stream_cipher():
    print("Enter the message you would like to encode below. (Note: It has to be in Binary)")
    stream_code = input("Message: ")
    print("Now enter a key that is the same length as the message that is also in Binary.")
    stream_key = input("Key: ")
    code_ints = [int(i) for i in str(stream_code)]
    key_ints = [int(i) for i in str(stream_key)]
    cipher_ints = []
    for x in range(len(code_ints)):
        cipher_bit = code_ints[x] ^ key_ints[x]
        cipher_ints.append(cipher_bit)
        cipher = "".join(str(b) for b in cipher_ints)
    print("Your encoded message: " + cipher)
