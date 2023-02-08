#Password Generator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

chose_letter = int(input("How many letters would you like in your password?\n"))
chose_symbol = int(input("How many symbols would you like?\n"))
chose_number = int(input("How many numbers would you like?\n"))
#easy
password_easy = ""
for chr in range(0,chose_letter):
    password_easy += random.choice(letters)
for chr in range(0,chose_number):
    password_easy += random.choice(numbers)
for chr in range(0,chose_symbol):
    password_easy += random.choice(symbols)
print(f"Your easy password is: {password_easy}")

#hard
password_list = []
for chr in range(0,chose_letter):
    password_list.append(random.choice(letters))
for chr in range(0,chose_number):
    password_list.append(random.choice(numbers))
for chr in range(0,chose_symbol):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)

password_hard = ""
for chr in password_list:
    password_hard += chr
print(f"Your hard password is: {password_hard}")








