"""Stage_2"""

# WIll create a MASTER password using HASHING
import os
import string
import json
import hashlib


def Master_Pass():

  print("LOGIN!!")

  while True:
    i=0
    with open("Password_Manager/Password_Manager1/master_password.json","r") as m_pass:
      try:
        data =json.load(m_pass)
      except Exception as e:
        print(e)
      
      Master = "Master_password"   # Key-pair
      print("Enter Master Password: ")
      in_put = input()
      salt ="X9@#"                  # applying salt in the value-pair
      in_put_salt = salt + in_put
      
      # value-pair successfully hashed
      hashed = hashlib.sha256(in_put_salt.encode()).hexdigest()
    
    
      if Master in  data and data[Master] == hashed:
        print("Password Verified ")
        break
      elif i==0 :
        print("Incorrect!!")
        print("\nTry again")
        i+=1