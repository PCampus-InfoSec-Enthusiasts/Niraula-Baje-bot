import hashlib

def encrypt(text):
    md = hashlib.md5(text.encode('ascii'))
    # print(md)
    salted = md.hexdigest() + text
    encrypted = hashlib.sha256(salted.encode('ascii'))
    return encrypted.hexdigest().split('\n')[0]

# txt = 'HEllo'
# print(encrypt(txt)) 
