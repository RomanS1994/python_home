# Caeser cipher / Affine cipher 

def encrypt(key, message):
    message = message.upper()
    result = ''
    alpha = 'ABCDEFGHIJKLMNOPRSTUVWXYZ'
    for letter in message:
        if letter in alpha:
            letter_index = (alpha.find(letter) + key) % len(alpha)
            result += alpha[letter_index]
        else:
            result += letter
    return result

encrypted_msg = encrypt(3, "brute is a killer horrible son")
print(encrypted_msg)