import os
import base64

from dotenv import load_dotenv

load_dotenv()

N = int(os.getenv('PUBLIC_KEY_N'))
e = int(os.getenv('PUBLIC_KEY_E'))
d = int(os.getenv('PRIVATE_KEY'))

def encrypt(message:str)->str:
    message_decimal = 0
    for char in message:
        if message_decimal == 0:
            message_decimal = (1 << 8)-1 & ord(char)
        else:
            message_decimal = (message_decimal << 8) | ord(char)
    
    cipher = pow(message_decimal, e, N)
    cipher_text = str(pow(cipher, e))
    cipher_bytes = cipher_text.encode("utf-8")
    return base64.b64encode(cipher_bytes).decode('utf-8')

def decrypt(cipher_text:str)->str:
    cipher_bytes = base64.b64decode(cipher_text)
    cipher_decimal = int(cipher_bytes.decode("utf-8"))
    cipher = int(round(cipher_decimal ** (1./3.)))
    plain_decimal = pow(cipher, d, N)
    plain_char = []
    while plain_decimal > 0:
        mask = (1 << 8) - 1
        char = plain_decimal & mask
        plain_char.append(chr(char))
        plain_decimal = plain_decimal >> 8
    plain_char.reverse()
    
    return ''.join(plain_char)

chiperrr = encrypt(input())
print(f"chiper = {chiperrr}")

plain = decrypt(chiperrr)
print(f"plain = {plain}")
