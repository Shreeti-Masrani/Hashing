import hashlib

str = input('Enter the string:: ')
print(str)

#using hash 3 diff hash algoriths
h1 = hashlib.sha256(str.encode())
h2 = hashlib.blake2b(str.encode())
h3 = hashlib.sha1(str.encode())

print("sh254 Algorithm   :: ",h1.hexdigest())
print("blake2b Algorithm :: ",h2.hexdigest())
print("sha1 Algorithm    :: ", h3.hexdigest())






