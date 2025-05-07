#Password generator

#Get password length from user, store in variable password_length
password_length = int(input("Enter the desired password length "))

#variables containing characteres that can be used to create a password
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!@#£%^&*()~-_'


#ask user which characters they want to use, store answers in variables
use_lowercase = input('Do you want to include lowercase letters in your password? Type yes/no ').lower()
use_uppercase = input('Do you want to include uppercase letters in your password? Type yes/no ').lower()
use_numbers = input('Do you want to include numbers in your password? Type yes/no ').lower()
use_symbols = input('Do you want to include symbols in your password? Type yes/no ').lower()


#empty string containing password characters chosen by user
character_pool = ''

#if user selected yes add to character_pool
if use_lowercase == 'yes':
    character_pool += lowercase_letters

if use_uppercase == 'yes':
    character_pool += uppercase_letters

if use_numbers == 'yes':
    character_pool += numbers

if use_symbols == 'yes':
    character_pool += symbols

#check which characters selected
print(character_pool)
