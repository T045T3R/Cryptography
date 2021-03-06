"""
cryptography.py
Author: Johannes Testorf
Credit: Wilson Rimberg

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
associations1 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
a=0
while a!=1:
    mode = str(input("Enter e to encrypt, d to decrypt, or q to quit: "))
    while not mode in ["e","d","q"]:
        print("Did not understand command, try again.")
        mode = str(input("Enter e to encrypt, d to decrypt, or q to quit: "))
    if mode == "q":
        print("Goodbye!")
        a=1
    if mode == "e":
        tochange = list(input("Message: "))
        key = list(input("Key: "))
        for x in range(0, len(tochange)):
            tochange[x]=associations.find(tochange[x])
            
        for x in range(0, len(key)):
            key[x]=associations.find(key[x])
        for x in range(0, len(tochange)):
                a=x//int(len(key))
                y=int(x-(a*len(key)))
                code= int(tochange[x]+key[y])
                print(associations1[code], end="")
        print()
    if mode == "d":
        tochange = list(input("Message: "))
        key = list(input("Key: "))
        for x in range(0, len(tochange)):
            tochange[x]=associations.find(tochange[x])
        for x in range(0, len(key)):
            key[x]=associations.find(key[x])-(associations.find(key[x])//87)
        for x in range(0, len(tochange)):
            a=x//int(len(key))
            y=int(x-(a*len(key)))
            code= int(tochange[x]-key[y])
            print(associations1[code], end="")
        print()