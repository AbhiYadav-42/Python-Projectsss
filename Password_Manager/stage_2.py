"""Stage_2"""

# WIll create a MASTER password using HASHING
import os
import string
import json
import hashlib
import getpass


def Master_Pass():

  print("LOGIN!!")

  while True:
    i=0
    with open("Password_Manager/Password_Manager1/master_password.json","r") as m_pass:
      try:
        data =json.load(m_pass)
      except Exception as e:
        print(e)
      
      salt ="X9@#"      # applying salt in the key-value-pairs
      
      Master = getpass.getpass(prompt="Enter Username: ")   # Key-pair
      Master_salt = Master + salt
      
      # key-pair successfully hashed
      hashed2 = hashlib.sha256(Master_salt.encode()).hexdigest()
      
      in_put = getpass.getpass(prompt="Enter Master Password: ")
      in_put_salt = salt + in_put
      
      # value-pair successfully hashed
      hashed = hashlib.sha256(in_put_salt.encode()).hexdigest()
    
    
      if hashed2 in data and data[hashed2] == hashed:
        print("Password Verified ")
        break
      else:
        print("Incorrect!!")
        while True: 
            wanna_try_again = input("wanna try again? (y/n): ")
            if wanna_try_again == "y":
                break
            elif wanna_try_again == "n":
                return False