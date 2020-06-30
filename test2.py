#!/usr/bin/env python3

"""
IMPORTING REQUIRED LIBRARIES
"""

from cryptography.fernet import Fernet
import os

"""
DEFINING FUNCTIONS TO LOAD AND DECRYPT XML FILES
"""

def load_key():
    return open("/datavolume1/key.key", "rb").read()
key = load_key()

def decrypt(filename, key):
    filenewname="/datavolume1/"+filename
    f = Fernet(key)
    with open(filenewname, "rb") as file:
        # read the encrypted data
        encrypted_data = file.read()
    # decrypt data
    decrypted_data = f.decrypt(encrypted_data)
    # write the original
    with open("/result/"+filename[0:-10]+".xml", "wb") as fill:
        fill.write(decrypted_data)


"""
SEARCHING THE FILES WHICH ARE ENCRYPTED AND DECRYPTING THE SAME USING LOADED KEY
"""

for root, dirs, files in os.walk("/datavolume1"):
    for file in files:
        if(file.endswith("_encrypted")):
            decrypt(file, key)

