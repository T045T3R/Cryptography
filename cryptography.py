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
    key = list(input("Key: "))
    for x in range(0, len(tochange)):
        tochange[x]=associations.find(tochange[x])
    for x in range(0, len(key)):
        key[x]=associations.find(key[x])
    for x in range(0, len(tochange)):
        y=x
        if x>len(key):
            a=x//len(key)
            y=x-(a*len(key))
        code=tochange[x]+key[y]
        print(code, end=" ")
    print()
            
        