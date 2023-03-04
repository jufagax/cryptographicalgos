alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

text = input("enter the plain text : ")
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

def reverse(text):
    rev=""
    i = len(text)-1
    for letter in text:
        rev += text[i]
        i-=1
    print(rev)
reverse(text)

def reverse2(text):
    rev = text[::-1]
    print(rev)

reverse2(text)