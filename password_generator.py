#Password generator

import random

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

#list of 1 character from each selected character type
mandatory_character = []

#if user selected yes add to character_pool and add 1 character to mandatory_character
if use_lowercase == 'yes':
    character_pool += lowercase_letters
    mandatory_character.append(random.choice(lowercase_letters))

if use_uppercase == 'yes':
    character_pool += uppercase_letters
    mandatory_character.append(random.choice(uppercase_letters))

if use_numbers == 'yes':
    character_pool += numbers
    mandatory_character.append(random.choice(numbers))

if use_symbols == 'yes':
    character_pool += symbols
    mandatory_character.append(random.choice(symbols))

print(mandatory_character)

#check if character_pool is empty
if not character_pool:
    print('Error: You must select at least one character type!')


else:
    #string to hold password
    final_password = ''

    #loop through selected characters, adding at random to final_password
    for number in range(password_length):
        random_char = random.choice(character_pool)
        final_password += random_char

    print(final_password)

