alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(p_text, shift_a):
    encry_word = ""
    for letter in p_text:
        position = alphabet.index(letter)
        new_pos = position + shift_a
        encry_word += alphabet[new_pos]
    print(encry_word)


def decrypt(e_text, shift_a):
    decry_word = ""
    for letter in e_text:
        position = alphabet.index(letter)
        new_pos = position - shift_a
        decry_word += alphabet[new_pos]
    print(decry_word)


if (direction.lower() == "encode"):
    encrypt(text, shift)
elif (direction.lower() == "decode"):
    decrypt(text, shift)

