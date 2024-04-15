import random

print("Welcome to Password Generator!")

num_letters = int(input('How many letters you want in your password\n'))

num_symbols = int(input('How many symbols you want in your password\n'))

num_numbers = int(input('How many numbers you want in your password\n'))

password_list = []

for i in range(1, num_letters+1):
    letter_char = random.choice(letters)
    password_list.append(letter_char)


for j in range(1, num_symbols+1):
    symbol_char = random.choice(symbols)
    password_list.append(symbol_char)


for k in range(1, num_numbers+1):
    num_char = random.choice(numbers)
    password_list.append(num_char)

random.shuffle(password_list)

password = ""

for char in password_list:
    password += char

print(password)