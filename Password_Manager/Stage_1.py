import os
import string
import json
import stage_2
#  Core Structure (No encryption) of your password manager project.


#  to do following task i need to use the funcitons
#  user says add then it should ask the website name 
#  ask for password 
#  can perferom view 
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
    with open("Password_Manager/Password_Manager1/password.json" ,"r") as pass_word:
      pass_dic = json.load(pass_word)
  except FileNotFoundError as e:
    print(e)

special_symbols = set(string.punctuation) 

def validation_pass(password):
  has_length= len(password) >=8
  has_digit = False
  has_symbol = False
  has_uppercase = False
  has_lowercase = False
  
  for char in password:
    if char.isdigit():
      has_digit = True
    elif char in special_symbols:
      has_symbol = True
    elif char.isupper():
      has_uppercase = True
    elif char.islower():
      has_lowercase = True
  
          
# Optional: Exit the loop early if all conditions are met
    if has_digit and has_symbol and has_uppercase and has_lowercase and has_length:
      break

  if has_lowercase and has_digit and has_symbol and has_uppercase and has_length:
    return True, "Password is Valid"
  else:
    Feedback = []
    if not has_digit:
      Feedback.append("Password must contains atleast one digit")
    if not has_length:
      Feedback.append("Password must contains atleast 8 values")
    if not has_symbol:
      Feedback.append("Password must contains atleast one symbol")
    if not has_uppercase:
      Feedback.append("Password must contains atleast one uppercase")
    if not has_lowercase:
      Feedback.append("Password must contains atleast one lowecase")
    return False ,"\n".join(Feedback)

def add():
  website = input("Website name: ")

  password = input("Password: ")
  
  p = validation_pass(password)       #  calling validation function
  
  # checking if the first element is true (validation is PASSED!!)
  if p[0] == True:
    global pass_dic
    pass_dic[website] = password
# FILE I/O of adding
    with open("Password_Manager/Password_Manager1/password.json", "w") as pass_word:
      json.dump(pass_dic,pass_word,indent=4)
    print("Password SAVED!!")     # SAVED!!
  else:
    print(p[1])     # Print the second element (The error part in the feedback list ) 

# VIEW
def view():
  global pass_dic
  print(pass_dic)  
load_passwords()


# calling the Master Password
if not stage_2.Master_Pass():
  exit()


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
