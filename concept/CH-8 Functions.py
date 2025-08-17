# A function is a group performing a specific task
# when a program gets bigger in size and its complexity grows, it gets difficult for a program to keep track on which piece of code  is doing what!!
  
# A function can be refused by the programmer in a given program any number of 

def func1():             #{  Funciton      }
  print('hello')         #{    definiton   }
func1()  # fucniton call


# WAP to greet a suser with "good day"
N=input("enter user name: ")
def greet():
  print(f" Have a Good day  {N}")
greet()
 
# Types of funiton 
"""
1. Built in funciton ( already present in python)
    -->> len(), print(), range()...etc

2. User defined fucnitons (Defined by the user )
  --> like  above  fucniton , greet(), func1()
"""


# fucntion with argumnet -->> A function can accept some value it can work with. We can put these values in the parentheses.


def goodday(name, ending):
  print("Good day, " + name)
  print(ending)

  return "done"   # by giving return , the 'a' will now contian goodday("Harry", " Thank you")


a = goodday("Harry", " Thank you")
goodday("Abhi", " Thank")
print(a)    # now when you try to print , it  will display the return value which is "done"


# default Argument
def goodday2(name, ending="thanks"):   # This the default parameter
  print(f"Good day {name} ")
  print(ending)


goodday2("Harry2")  # this will autmoatically put the default value in the ending 



# RECURSION -->> It is a funciton which call itself

"""
factorial (0) = 1
factorial (1) = 1
factorial (2) = 2 x 1
factorial (3) = 3 x 2 x 1
factorial (4) = 4 x 3 x 2 x 1
factorial (5) = 5 x 4 x 3 x 2 x 1
"""
def factorial(n):
  if(n==0 or n==1):
    return 1
  return n*factorial(n-1)


n= int(input("Enter number: "))
print(f" The factorial is : {factorial(n)}")