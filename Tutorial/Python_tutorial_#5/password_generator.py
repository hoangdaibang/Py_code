'''
Project name :
    Ramdom Password Gennerator 

'''
from ast import Str
from lib2to3.pgen2.token import NUMBER
from operator import truediv
from re import A
import string
import random

LETTERS = string.ascii_letters
NUMBER = string.digits
PUCTUATION =string.punctuation 


def password_generator(lenght):
    printable = f"{LETTERS}{NUMBER}{PUCTUATION}"
    printable = list(printable)
    random.shuffle(printable)
    random_password = random.choices(printable, k=lenght)
    
    random_password = "".join(random_password)

    return(random_password)


def get_password_length():
    while True:
        password_length = input("Please enter length of password :")
        if password_length:
            if password_length in NUMBER: 
                password_length = int(password_length)
                return(password_length)
            else:
                continue
        else:
            continue



def main():
        length = get_password_length()
        password = password_generator(length)
        print(password)


if __name__ == "__main__" :
    main()

