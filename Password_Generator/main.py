import random
import string

letter = string.ascii_letters
degits = string.digits
special = string.punctuation

length_pass = int(input("Enter the length of password : "))

digits_pass = input("Do you want digits in password (True/False) : ")
if digits_pass == "True":
    digits_pass == True
else:
    digits_pass == False

special_pass = input("Do you want Special Chars in password (True/False) : ")
if special_pass == "True":
    special_pass == True
else:
    special_pass == False

all = ""
if letter:
    all += letter
if degits:
    all +=degits 
if special:
    all +=special

amount_password = 5


for i in range(amount_password):
    password = "".join(random.sample(all,length_pass))
    print(password)
