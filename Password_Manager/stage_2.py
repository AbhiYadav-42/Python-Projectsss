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
      
      Master = "Master_password"
      print("Enter Master Password: ")
      in_put = input()
      if Master in  data and data[Master] ==in_put:
        print("Password Verified ")
        break
      elif i==0 :
        print("Incorrect!!")
        print("\nTry again")
        i+=1