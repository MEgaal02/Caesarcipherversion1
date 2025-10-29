# A function with key parameters that's set the arguments of our user inputs in the while loop

# A string accumulator which collects our message through each loop one letter at time

# if the user's input in direction is decoded

#the shift will be switched to a negative using simple maths equation shift_number = shift_number * -1

#within the caesar function this for loops through every letter within user's input called message which is defined as text in the function


#a condition within the for loop which checks if letter input is not in alphabet for example a space


#if it isn't then the letter is added to our empty string accumulator in hte position the user inputted it in


#else if the letter in user input  is in the alphabet then based on whether it is encoded or decode , the letter shift's + or -


#the user inputted message for each letter is found located in our alphabet using index and added to shift amount


#the result of the final position in our alphabet is then modulo against the len of alphabet so if the user shifts past z, there will be a remainder so the letter will shift to that remainder


#finally all the letters in the loop are accumulated and added to our string variable


# The string variable output is then printed with all the shifted letters from users original input


# A typical while loop based on whether the user wants to continue or not


#while the user does want to continue:


# the input variables below are printed and the users data will be saved in the variables
direction (encode_or_decode in function, message text in function and shift which is shift number in function)

# as soon as the user inputs are saved the function caesar is then run to execute the encryption or decryption


#if user wants to continue or not


# if user does not want to continue the program is then halted with the code below


#else if the user does want to continue then the code loop back to our while loop inputs above
