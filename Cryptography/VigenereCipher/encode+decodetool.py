import math

def enc(pt):
    key = input("Key: ")
    keylist=[]
    ct="" #ciphertext
    start = ord('A')
    for i in range(0,len(pt)):
        k = i % len(key)
        keylist.append(key[k])
    for m in range(0,len(pt)):
        shift = ord(keylist[m])-start
        pos = start + (ord(pt[m]) + shift - start)%26
        ct = ct + chr(pos)
    return ct

def dec(ct):
    key = input("Key: ")
    keylist=[]
    pt="" #ciphertext
    start = ord('A')
    for i in range(0,len(ct)):
        k = i % len(key)
        keylist.append(key[k])
    for m in range(0,len(ct)):
        shift = ord(keylist[m])-start
        pos = start + (ord(ct[m]) + 26 - ord(keylist[m]))%26
        pt = pt + chr(pos)
    return pt


while True:
    choice = str(input("Encrypt(E) or Decrypt(D): "))
    if choice == "E":
        pt = str(input("Plaintext (upperscae): "))
        print(enc(pt))
    elif choice == "D":
        ct = str(input("Ciphertext (upperscae): "))
        print(dec(ct))
    else: break


