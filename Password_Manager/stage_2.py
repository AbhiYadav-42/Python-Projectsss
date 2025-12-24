"""Stage_2"""

# WIll create a MASTER password using HASHING
import os
import string
import json
import hashlib
import getpass

def hash_Value(value:str)-> str:
  return hashlib.sha256(value.encode()).hexdigest()

MASTER_FILE = "Password_Manager/Password_Manager1/master_password.json"
salt ="X9@#"

def Master_Pass():
  print("LOGIN!!")

#checking File existence!!
  if not os.path.exists(MASTER_FILE):
    print("Master password file not found!!")
    return False

#Load data
  try:
    with open(MASTER_FILE,"r") as m_pass:
      data =json.load(m_pass)
  except Exception as e:
      print(e)
      return False


  while True:      
        Master = input("Enter Username: ")   # Key-pair
        in_put = getpass.getpass(prompt="Enter Master Password: ")    # Value-pair

        # key-pair successfully hashed and salted
        hashed2 = hash_Value(Master + salt)
        hashed = hash_Value(salt+in_put)

        if hashed2 in data and data[hashed2] == hashed:
          print("✅ Password Verified!!")
          return True
        else:
          print("❌ Incorrect credentials!!")


          wanna_try_again = input("wanna try again? (y/n): ")
          if wanna_try_again != "y":
            return False
