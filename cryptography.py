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
    print("Did not understand command, try again.")
    mode = str(input("Enter e to encrypt, d to decrypt, or q to quit: "))
if mode == "q":
    print("Goodbye!")
if mode == "e":
    tochange = list(input("Message: "))
    key = input("Key: ")
    for x in range(0, len(tochange)):
        tochange[x]=associations.find(tochange[x])
        