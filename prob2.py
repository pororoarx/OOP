# LAB EXERCISE No 1
# Name: KEN ANDREA G. LEGASPI; Section: BSCPE 1-4
# PROBLEM 2

# Import the pyfiglet module for different fonts
import pyfiglet 

# Set and print the title of the activity in color and different font
title_of_assign = "Lab Exercise 1"
print(pyfiglet.figlet_format(title_of_assign))

# Create a class called "Decryption"
class Decryption:
    def __init__(self, input_str):
        self.input_str = input_str
        
    # Inside the class, create and initialize a function "decrypt" that takes an input string
    def decrypt(self):
        # Create a variable called "output_str"
        output_str = ""
        # Loop through each character in the input string
        for i in range(len(self.input_str)):
            # If the character is an asterisk, add "a" to the output_str
            if self.input_str[i] == '*':
                output_str += 'a';
            # If the character is an ampersand, add "e" to the output_str
            elif self.input_str[i] == '&':
                output_str += 'e';
            # If the character is a hash symbol, add "i" to the output_str
            elif self.input_str[i] == '#':
                output_str += 'i';
            # If the character is a plus symbol, add "o" to the output_str
            elif self.input_str[i] == '+':
                output_str += 'o';
            # If the character is an exclamation point, add "u" to the output_str
            elif self.input_str[i] == '!':
                output_str += 'u';
            else:
                output_str += self.input_str[i]
        # Return the output_str
        return output_str.strip()

# Ask the user to input a string
input_str = input("\033[96mEnter an input string: ")
# Create a new object of the Decryption class and the input string of the user
decryption_act = Decryption(input_str)
# Call the decrypt function and create a variable called output_str to get the results or decrypted output
output_str = decryption_act.decrypt()

# Print the output string in color
print("\033[92mThe output string is:", output_str)
print("\033[95m" + "=".ljust(40, "="))