# LAB EXERCISE No 1
# Name: KEN ANDREA G. LEGASPI; Section: BSCPE 1-4
# Problem 3

# Import the pyfiglet module for different fonts
import pyfiglet

# Set and print the title of the activity in color and different font
title_of_assign = "Lab Exercise 1"
font = "slant"
print("\033[38;5;206m", pyfiglet.figlet_format(title_of_assign, font=font))

# Ask user to enter plaintext message and keyword in all uppercase letters, no spaces. Make the plaintext and keyword in uppercase.
plaintext = input("\033[38;5;202mEnter your plaintext (all uppercase letters, no spaces): ")
plaintext = plaintext.upper()

keyword = input("\033[38;5;204mEnter your keyword (all uppercase letters): ")
keyword = keyword.upper()

# Create a class called "Vigenere_Cipher" that takes plaintext and keyword as an input
class Vigenere_Cipher:
    # Inside the class, initialize the class with the plaintext and keyword
    def __init__(self, plaintext, keyword):
        self.plaintext = plaintext.upper()
        self.keyword = keyword.upper()
        self.key_letter = [ord(letter) - 65 for letter in self.keyword]

    # Create a function called "cipher" to define the cipher method for the Vigenere_Cipher class
    def cipher(self):
        # Create an empty string "ciphertext"
        ciphertext = ""
        # Set the variable "keyword_letter" to 0
        keyword_letter = 0

        # Loop through each letter in the plaintext and encrypt each letter with Vigenere_Cipher
        for i in range(len(self.plaintext)):
            current_plain_letter = self.plaintext[i]
            key_number = self.key_letter[keyword_letter % len(self.keyword)]
            cipher_number = (ord(current_plain_letter) - 65 + key_number) % 26
            ciphertext += chr(cipher_number + 65)
            keyword_letter = (keyword_letter + 1) % len(self.keyword)

        # Return the ciphertext string
        return ciphertext

# Create a new object of the Vigenere_Cipher
# Execute the cipher method
vcipher = Vigenere_Cipher (plaintext.upper(), keyword.upper())
cipher_text = vcipher.cipher()

# Print the cipher text message in color
print("\033[92mThe secret code is:")
print("\033[95m" + cipher_text)
