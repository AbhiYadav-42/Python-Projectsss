#Write a program to create an dicitionary of hindi words with the values of English transaltion 
"""Q-1
DIC ={ 
  "pustak" : "book",  
  "paani" : "water", 
  "aadmi" : "man  ",
  "aurat" : "woman" , 
  "ghar" : "house"  ,
  "billi" : "cat  ",
  "kutta" : "dog  ",
  "sooraj" : "sun  ",
  "chaand" : "moon " ,
  "ped" : "tree " ,
  "phal" : "fruit" , 
  "doodh" : "milk " ,
  "khidki" : "window" , 
  "darwaza" : "door ", 
  "school" : "school" , 
  "khel" : "game " ,
  "dost" : "friend"  ,
 "khushi" : "happiness" , 
  "dukh" : "sorrow"  ,
  "prem" : "love"}

wORD=input("Enter the word:")
print(DIC[wORD])
"""

#Write a program to input 8 unique numbers from the users and display at once  
""" Q-2
s=set()
n=input("Enter the first number")
s.add(int(n))

n=input("Enter the first number")
s.add(int(n))

n=input("Enter the first number")
s.add(int(n))

n=input("Enter the first number")
s.add(int(n))

n=input("Enter the first number")
s.add(int(n))

n=input("Enter the first number")
s.add(int(n))

n=input("Enter the first number")
s.add(int(n))

n=input("Enter the first number")
s.add(int(n))

print(s)
"""

# Can we have a set of 18(int) and '18'(stri) as a value in it 
"""Q-3"""
s=set()
s.add(int(18))
s.add("18")
print(s)

# What will be the length of the foollwing set 
s= set()
s.add(20)
s.add(20.0)
s.add('20')

#s={}
#  what is the type 's' 
"""  it is an empty disctionary , not a set because empty{} denotes a dictionary and to denote empty set is like this s()"""

# Create an empty  dictionary. Allow 4 friends to enter their favourite language as value and use thier name as key.
"""Q-6"""
d={}

F=input("Enter Friends's name:")
L=input("Enter the lanugage name:")

d.update({F:L})

F=input("Enter Friends's name:")
L=input("Enter the lanugage name:")

d.update({F:L})

F=input("Enter Friends's name:")
L=input("Enter the lanugage name:")

d.update({F:L})

F=input("Enter Friends's name:")
L=input("Enter the lanugage name:")

d.update({F:L})
print(d)
#