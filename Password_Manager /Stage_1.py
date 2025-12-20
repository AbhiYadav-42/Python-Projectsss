import os
import string
#  Core Structure (No encryption) of your password manager project.


#  to do following task i need to use the funcitons
#  user says add then it should ask the website name 
#  ask for password 
#  save it in a file (JSON)

#
pass_dic = {
# "wesbite_name" : "password"
  " github" : " Abhi@123",
  "abhi@gmail.com" : "1Abhi@321"
}

def load_passwords():
  global pass_dic
  try:
    with open("Password_Manager /Password_Manager1/password.txt" ,"r") as pass_word:
      for line in pass_word:
        if ":" in line:
          website, password = line.strip().split(":",1)
          pass_dic[website.strip()] = password.strip()
  except FileNotFoundError:
    pass


def validation_pass(password):
  has_digit = False
  has_symbol = False
  has_uppercase = False
  has_lowercase = False
  for char in password:
    if char.len(password) < 9:
      print(" should contain atleast 8 ")
    elif char.isdigit():
      has_digit = True
    elif char.isalnum():
      has_symbol = True
    elif char.isupper():
      has_uppercase = True
    elif char.islower():
      has_lowercase
      
#   it is for when all are conditions are met!! 
    if has_lowercase and has_digit and has_symbol and has_uppercase :
      return True, "Password is Valid"


def add():
  website = input("Website name: ")

  password = input("Password: ")
  validation_pass(password)

  global pass_dic
  pass_dic[website] = password

# FILE I/O

  with open("Password_Manager /Password_Manager1/password.txt","a") as pass_word:
    pass_word.write(f"{website}: {password}\n")
  return print("done")
  
def view():
  global pass_dic
  print(pass_dic)  
  
load_passwords()

while True:
  print("Do You wanna add a mew password or view exisitng ones? ")
  us_in = input()
  if us_in.lower() == "add":
    add()
  elif us_in.lower() == "view":
    view()
    
  play_again = input("wanna do something else?(y/n): ")
  if play_again != "y":
    break
  