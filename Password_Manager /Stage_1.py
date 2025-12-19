import os
#  Core Structure (No encryption) of your password manager project.


#  to do following task i need to use the funcitons
#  user says add then it should ask the website name 
#  ask for password 
#  save it in a file 

#
pass_dic = {
# "wesbite_name" : "password"
  " github" : " Abhi@123",
  "abhi@gmail.com" : "1Abhi@321"
}
def add():
  website = input("Website name: ")
  password = input("Password: ")
  
  global pass_dic
  pass_dic[website] = password

# FILE I/O

  with open("Password_Manager /Password_Manager1/password.txt","w") as pass_word:
    pass_word.write(f"{website}: {password}\n")
  return print("done")
  
def view():
  global pass_dic
  print(pass_dic)  

 
while True:
  manager = print("Do You wanna add a mew password or view exisitng ones? ")
  us_in = input()
  if us_in.lower() == "add":
    add()
  elif us_in.lower() == "view":
    view()
    
  play_again = input("wanna do something else?(y/n): ")
  if play_again != "y":
    break
  