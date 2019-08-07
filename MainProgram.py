import Caesar
import DecodeCaesar
import Block
import Stream


def newmessage_ask():
    print("Would you like to encode or decode a new message?")
    newmessage_choice = input("Yes/No: ").lower()
    if newmessage_choice == "yes":
        print("Ok.")
        main()
    elif newmessage_choice == "no":
        print("Ok. Thank You for using our program.")


def no_confirm():
    print("Would you like to start over?")
    startover_choice = input("Yes/No: ").lower()
    if startover_choice == "yes":
        print("You are now starting over.")
        main()
    else:
        print("Ok. Thank You for using our Program.")


def main():
    print("Would you like to encode a message?")
    first_choice = input("Encode/Decode: ").lower()
    if first_choice == "encode":
        print("You have chosen to Encode a message.")
        print("Would you like to continue?")
        encode_confirm_choice = input("Yes/No: ").lower()
        if encode_confirm_choice == "yes":
            print("You may choose between the following ciphers:")
            print("1. Caesar Cipher (Easiest to decode)")
            print("2. Stream Cipher (For Messages in Binary, almost impossible to decode without the key)")
            print("3. Block Cipher (Almost impossible to decode without the key.")
            print("Which one would you like to use?")
            encode_cipher_choice = int(input("1/2/3: "))
            if encode_cipher_choice == 1:
                print("You have selected to encode a message using the Caesar Cipher.")
                print("Is this correct?")
                caesar_cipher_confirm_choice = input("Yes/No: ").lower()
                if caesar_cipher_confirm_choice == "yes":
                    print("Great.")
                    Caesar.encode_caesar_cipher()
                    newmessage_ask()
                elif caesar_cipher_confirm_choice == "no":
                    no_confirm()
                else:
                    print("Invalid Input. Starting Over.")
                    main()
            elif encode_confirm_choice == 3:
                print("You have selected to encode a message with the Block Cipher.")
                print("Is this Correct?")
                block_cipher_confirm_choice = input("Yes/No: ").lower()
                if block_cipher_confirm_choice == "yes":
                    print("Great.")
                    Block.encode_block_cipher()
                    newmessage_ask()
                elif block_cipher_confirm_choice == "no":
                    no_confirm()
                else:
                    print("Invalid Input. Starting Over.")
                    main()
            elif encode_cipher_choice == 2:
                print("You have selected to encode a string of binary numbers using the Stream Cipher.")
                print("Would you like to continue?")
                stream_cipher_confirm_choice = input("Yes/No: ").lower()
                if stream_cipher_confirm_choice == "yes":
                    print("Great.")
                    Stream.encode_stream_cipher()
                    newmessage_ask()
                elif stream_cipher_confirm_choice == "no":
                    no_confirm()
                else:
                    print("Invalid Input. Starting Over.")
                    main()
        elif encode_confirm_choice == "no":
            no_confirm()
        else:
            print("Invalid Input. Starting Over.")
            main()
    elif first_choice == "decode":
        print("Right now the only cipher we have support for decoding is the Caesar Cipher.")
        print("Would you like to continue?")
        decode_confirm_choice = input("Yes/No: ")
        if decode_confirm_choice == "yes":
            print("Great.")
            print("Enter the message you want to decode below.")
            caesar_decode_message = input("Message: ")
            DecodeCaesar.decode_caesar_cipher(caesar_decode_message)
            newmessage_ask()
        elif decode_confirm_choice == "no":
            no_confirm()
        else:
            print("Invalid Input. Starting over.")
    else:
        print("Invalid Input. Starting Over.")
        main()


print("Welcome to our program!")
print("Right now we can help you to encode and decode messages using different Shift Ciphers.")
main()
