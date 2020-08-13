#! /usr/bin/python3 
# /usr/bin/python2
import hashlib

def encrypt(text):
    md = hashlib.md5(text)
    salted = md.digest() + text
    encrypted = hashlib.sha256(salted)
    return encrypted.digest().split('\n')[0]

txt = 'HEllo'
b_txt = txt.encode()
print(type(b_txt)) 





'''

# o_txt = 'HEllo'
# txt = o_txt.encode('utf-8')
md = hashlib.md5(b'helllo')
salted = md + text.to_bytes    #here's the problem

# salted=b'\x9c(\x1a\x0e\xf8\x1e%t\x07\xfe\x01\xfaj\xa0\xfashelllo'

encrypted = hashlib.sha256(salted)
e = encrypted.digest()
f = e.decode('utf-8').split('\n')[0]   #here is the major one, caused due to above
print(e)

'''