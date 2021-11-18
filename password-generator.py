#Password Generator Project

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("\n------------ Welcome to the PyPassword Generator! --------------\n")
nr_letters= int(input("\nHow many letters would you like in your password?\n")) 
nr_symbols = int(input(f"\nHow many symbols would you like?\n"))
nr_numbers = int(input(f"\nHow many numbers would you like?\n"))

seed = random.randint(0,10000)
random.seed(seed)

r_letters = []
for n in range(0, nr_letters):
    r_letters.append(letters[random.randint(0,len(letters)-1)])


r_numbers = []
for n in range(0, nr_numbers):
    r_numbers.append(numbers[random.randint(0,len(numbers)-1)])


r_symbols = []
for n in range(0, nr_symbols):
    r_symbols.append(symbols[random.randint(0,len(symbols)-1)])


gen_password = r_letters + r_numbers + r_symbols
random.shuffle(gen_password)

generated_password = "".join(gen_password)

print(f"\nYour new password is: {generated_password}\n\n")

