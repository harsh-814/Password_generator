import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
num = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
symbol = ["!", "@", "#", "$", "%"]
nr_letters = int(input("How many Letters do you wants in your password?\n"))
nr_num = int(input("How many numbers do you wants in your Password?\n"))
nr_symbols = int(input("How many symbols do you wants in your Password?\n"))
password = []
for randoms in range(1,nr_letters+1):
    select = random.choice(letters)
    password += select
for randoms in range(1,nr_num+1):
    select = random.choice(num)
    password += select
for randoms in range(1,nr_symbols+1):
    select = random.choice(symbol)
    password += select
random.shuffle(password)
password_str = ""
for char in password:
    password_str += char
print(f"Your password is {password_str}")