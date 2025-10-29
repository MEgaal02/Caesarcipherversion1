import art

print(art.logo)


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']




def caesar(encode_or_decode, text, shift_number ):


    output_text = ""

    if encode_or_decode == "decode":
        shift_number *= -1



    for letter in text:

        if letter not in alphabet:
            output_text += letter

        else:


            shifted_position = alphabet.index(letter) + shift_number
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]



    print(f"Here is your {encode_or_decode}d result: {output_text}")


should_continue = True
while should_continue:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n ").lower()
    if direction != "encode" and "decode":
        print("Wrong selection")
        yes_or_no = input("Type 'yes' if you want to go again. Otherwise type 'no'.").lower()

        if yes_or_no == "no":
             should_continue = False


    else:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n ").lower()
        message = input("Type your message:\n ").lower()
        shift = int(input("Type the shift number:\n "))

        caesar(encode_or_decode=direction, text=message, shift_number=shift)






