# Copyright [2020] <eyadali05> [GNU GENERAL PUBLIC LICENSE]
# The purpose of this script is to generate a strong password and to copy it

import random # to choose random chars from pwdchars.txt
import pyperclip # copy to clipboard

class Generator:
    def __init__(self):
        super().__init__()

    def generate_pwd(self):
        pwdchars = ""
        pwd = ""
        with open("pwdchars.txt", "r") as charsfile:
            pwdchars = charsfile.read()
        pwd_length = int(input("Enter your password length: "))
        for char in range(pwd_length):
            pwdchar = random.choice(pwdchars)
            pwd = pwd + pwdchar 
        pyperclip.copy(pwd)
        print("Password generated and copied to clipboard successfully! \n")
        return pwd
