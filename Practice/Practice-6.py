# Write a program to find the greatest of four numbers entred by the user!
"""Q-1"""
A=int(input("Enter number:"))
B=int(input("Enter number:"))
C=int(input("Enter number:"))
D=int(input("Enter number:"))

if(A>B and A>C and A>D):
  print("A is the greatesT number:",A)

elif(B>A and B>C and B>D):
  print("B is the greatesT number:",B)

elif(C>A and C>B and C>D):
  print("C is the greatesT number:",C)

elif(D>B and D>C and D>A):
  print("D is the greatesT number:",D)

  
# Write a program to find out whether a student has passed or failed if it requires a total 40% and atleast 33% in each subject to pass. Assume 3 subject and takes marks as an input from the user.
"""Q-2"""
# Marks of 3 subject
m=int(input(" 1st subject:"))
a=int(input(" 2nd subject:"))
r=int(input(" 3rd subject:"))

k=(m+a+r)*100/300 
print("percentage of 3 subject:",k)

if(k>40 and m>=33 and a>=33 and r>=33):
  print("You PASSED!!")

else:
  print("You FAILED!!")


if(k>90 and k<=100):
  print("EXECLLENT!!!!")

elif(k>86 and k<=90):
  print("VERY GOOD!!")

elif(k>75 and k<=86):
  print("GOOD!!")

elif(k>70 and k<=75):
  print("YOU CAN DO BETTER!!")

elif(k<=70 and k>=65):
  print("WORK HARD!!")

elif(k==33):
  print("POOR!!")


# #A spam comment is defined as a text containing following keywords:
# "Make a lot of money", "buy now", "subscribe this", "click this". write a program to detect these spam messages 

"""Q-3"""
# spam filter system
s1= "Make a lot of money"
s2= "make a lot of money"

s3= "Buy now"
s4 = "buy now"

s5 = "Subscribe this"
s6 = "subscribe this"

s7= "click this"
s8= " Click this"

message=input("Comment here: ")

if((s1 and s2 in message) or (s4 and s3 in message ) or (s5 and s6 in message) or (s7 or s8 in message)):
  print("it's a spam comment")

else:
  print("it is not valid comment ")



#write a program to find whether a given username contains less than 10 characters or not

"""Q-4 """

Username=input("Create your username:")

if(len(Username)<10):
  print("It should atleast of 10 characters!!")

else:
  print("valid username!!")


#Write a program which finds out whether a given name is present or not 

n=input("Enter the name: ")
st="Abhi "

if(st==n):
  print("yes, given name is present")

else:
  print("no, given name is not present ")




























