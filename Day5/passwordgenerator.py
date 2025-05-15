import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = int(input("How many letters do you want: "))
nr_numbers = int(input("How many numbers do you want: "))
nr_symbols = int(input("How many symbols do you want: "))

random_letters = random.sample(letters, nr_letters)
random_numbers = random.sample(numbers, nr_numbers)
random_symbols = random.sample(symbols, nr_symbols)

joined_letters = "".join(random_letters)
joined_numbers = "".join(random_numbers)
joined_symbols = "".join(random_symbols)

password = joined_letters + joined_numbers + joined_symbols

password_list = list(password)
random.shuffle(password_list)
shuffled_password = "".join(password_list)

print(f"Your structured password is {password}")
print(f"Your shuffled password is {shuffled_password}")