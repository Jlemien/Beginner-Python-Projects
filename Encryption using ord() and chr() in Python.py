message = input("Enter a message to encrypt: ").upper()
encrypted = ""

for letter in message:
    if letter == " ":
        encrypted += " "
    elif ord(letter) + 5 > ord("Z"):
        encrypted += chr(ord(letter) + 5 - 26)

    else:
        encrypted += chr(ord(letter) + 5)

print(encrypted)
