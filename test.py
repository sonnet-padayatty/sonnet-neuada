#!/usr/bin/env python3

"""
IMPORTING REQUIRED LIBRARIES
"""

from json2xml import json2xml
from json2xml.utils import readfromjson
from cryptography.fernet import Fernet
import os
import shutil

"""
DEFINING REQUIRED FUNCTIONS TO GENERATE & LOAD KEY
"""

def write_key():
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    with open("/datavolume1/key.key", "wb") as key_file:
        key_file.write(key)
def load_key():
    """
    Loads the key from the current directory named `key.key`
    """
    return open("/datavolume1/key.key", "rb").read()

"""
CHECKS THE EXISTENCE OF KEY IN THE SHARED DATAVOLUME TO GENERATE NEW ONE
"""

check="yes"
for root, dirs, files in os.walk("/datavolume1"):
    for file in files:
        if(file.endswith(".key")):
            check="no"
if(check=="yes"):
	write_key()

key = load_key()

"""
FINDING THE FILES WHICH ARE IN JSON FORMAT
CONVERTING THE JSON FILES TO XML FORMAT
ENCRYPTING THE XML FILES USING THE KEY GENERATED ABOVE
MOVING THE FILES TO DATAVOLUME1
"""

for root, dirs, files in os.walk("/"):
    for file in files:
        if(file.endswith(".json")):
            fp=os.path.join(root, file)
            fpp=os.path.join(file)
            if not (fp[0:4]=="/usr"):
                data = readfromjson(fp)
                fil=open(fp[0:-5]+".xml",'w')
                print(json2xml.Json2xml(data).to_xml(),file=fil)
                fil.close()
                with open(fp[0:-5]+".xml", "rb") as ff:
                    x_data = ff.read()
                f = Fernet(key)
                encrypted_data = f.encrypt(x_data)
                os.remove(fp[0:-5]+".xml")
                with open(fp[0:-5]+"_encrypted", "wb") as fi:
                    fi.write(encrypted_data)
                shutil.move(fp[0:-5]+"_encrypted","/datavolume1/"+fpp[0:-5]+"_encrypted")

