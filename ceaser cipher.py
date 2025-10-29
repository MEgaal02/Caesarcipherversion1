import art#imported logo from separate file and displayed below

print(art.logo)


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']# a list with the corresponding letters in the alphabet




def caesar(encode_or_decode, text, shift_number ):# A function with key parameters that's set the arguments of our user inputs in the while loop


    output_text = "" # A string accumulator which collects our message through each loop one letter at time

    if encode_or_decode == "decode": # if the user's input in direction is decoded
        shift_number *= -1  #the shift will be switched to a negative using simple maths



    for letter in text:#within the caesar function this for loops through every letter within user's input called message which is defined as text in the function

        if letter not in alphabet:#a condition within the for loop which checks if letter input is not in alphabet for example a space
            output_text += letter #if it isn't then the letter is added to our empty string accumulator in hte position the user inputted it in

        else: #else if the letter in user input  is in the alphabet then based on whether it is encoded or decode , the letter shift's + or -


            shifted_position = alphabet.index(letter) + shift_number#the user inputted message for each letter is found located in our alphabet using index and added to shift amount
            shifted_position %= len(alphabet)#the result of the final position in our alphabet is then modulo against the len of alphabet so if the user shifts past z, there will be a remainder so the letter will shift to that remainder
            output_text += alphabet[shifted_position]#finally all the letters in the loop are accumulated and added to our string variable



    print(f"Here is your result: {output_text}")# The string variable output is then printed with all the shifted letters from users original input


should_continue = True# A typical while loop based on whether the user wants to continue or not
while should_continue:#while the user does want to continue:
    # the input variables below are printed and the users data will be saved in the variables

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n ").lower()
    message = input("Type your message:\n ").lower()
    shift = int(input("Type the shift number:\n "))

    caesar(encode_or_decode= direction, text= message, shift_number= shift)# as soon as the user inputs are saved the function caesar is then run to execute the encryption or decryption

    yes_or_no = input("Type 'yes' if you want to go again. Otherwise type 'no'.").lower()#if user wants to continue or not

    if yes_or_no =="no":  # if user does not want to continue the program is then halted with the code below
        should_continue = False
        print("Goodbye")
        break

    #else if the user does want to continue then the code loop back to our while loop inputs above








