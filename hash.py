import hashlib

s = input('Enter the string:: ')
print(s)
h = hashlib.md5(s.encode())
print(h.hexdigest())

