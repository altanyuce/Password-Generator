import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
letter = int(input("How many letters would you like in your password? "))
symbol = int(input("How many symbols would you like? "))
number = int(input("How many numbers would you like? "))

password_easy = ""
password_hard = ""
password_list = []
for i in range(0, letter):
    password_easy += random.choice(letters)
for i in range(0, symbol):
    password_easy += random.choice(symbols)
for i in range(0, number):
    password_easy += random.choice(numbers)

password_list = list(password_easy)
random.shuffle(password_list)
password_hard = "".join(password_list)


print(f"Your easy password is: {password_easy}")
print(f"Your hard password is: {password_hard}")







