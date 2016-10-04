"""
cryptography.py
Author: Johannes Testorf
Credit: Wilson Rimberg

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"

mode = str(input("Enter e to encrypt, d to decrypt, or q to quit: "))
while not mode in ["e","d","q"]:
    mode = str(input("Enter e to encrypt, d to decrypt, or q to quit: "))
if mode == "q":
    print("Goodbye!")
