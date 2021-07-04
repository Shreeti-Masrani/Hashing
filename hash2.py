import hashlib
import os

s = os.urandom(32)
str = input('Enter str:: ')

k1 = hashlib.pbkdf2_hmac('sha256',str.encode('utf-8'),s,1000)
k2 = hashlib.pbkdf2_hmac('md5',str.encode('utf-8'),s,1000)
print('-------Salt-------')
print(s)
print('-------key of sha256 algo-------')
print(k1)
print('-------key of md5 algo-------')
print(k2)
