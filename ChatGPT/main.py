import random
import string

print("Welcome to the PyPassword Generator!")

nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Use string.ascii_letters and string.digits to generate lists of letters and numbers
letters = list(string.ascii_letters)
numbers = list(string.digits)
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password_list = []

# Use random.sample to randomly select characters without replacement
password_list += random.sample(letters, nr_letters)
password_list += random.sample(symbols, nr_symbols)
password_list += random.sample(numbers, nr_numbers)

# Use random.shuffle to shuffle the list of characters
random.shuffle(password_list)

password = "".join(password_list)
print(f"Your password is: {password}")

# This script eliminates the need for a loop to append individual characters to the password list. It instead uses the random.sample function to 
# randomly select the specified number of characters from the letters, symbols, and numbers lists, and appends them to the password_list. 
# It also uses string.ascii_letters and string.digits to generate the letters and numbers list, instead of hardcoding it.

# This script also uses the join() function to join the list of characters into a single string, instead of looping through the list and concatenating each character.