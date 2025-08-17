# Create a class "Programmer" for storing information of few programmers working at Microsoft.
"""Q-1
class Programmer:
  company ="Microsoft"
  def __init__(self,name , salary , lan, state ):
    self.name=name 
    self.salary = salary
    self.lan = lan
    self.state= state
print("The programmers description 👇\n")

Abhi=Programmer("Abhi", " 120000", "Python", "U.P")
print(f"name ->{Abhi.name}, salary ->{Abhi.salary}, Master in language -> {Abhi.lan}\n, Working at-> {Abhi.company}, State -> {Abhi.state}")

Ani=Programmer("Abhi", " 120000", "JavaScript", "M.P")
print(f"\nname ->{Ani.name}, salary ->{Ani.salary}, Master in language -> {Ani.lan}\n,Working at{Abhi.company} ,State -> {Ani.state}\n")

Adi=Programmer("Abhi", " 120000", "Java", "DELHI")
print(f"\nname ->{Adi.name}, salary ->{Adi.salary} ,Master in language -> {Adi.lan}\n, Working at-> {Abhi.company} ,State -> {Adi.state}\n")

Ayan=Programmer("Abhi", " 120000", "Python", "A.P")
print(f"\nname ->{Ayan.name} ,salary ->{Ayan.salary} ,Master in language -> {Ayan.lan}\n , Working at ->{Abhi.company},State -> {Ayan.state}\n")

keshav=Programmer("keshav", " 120000", "C", "M.P")
print(f"\nname ->{keshav.name}, salary ->{keshav.salary}, Master in language -> {keshav.lan}\n, Working at-> {Abhi.company}, State -> {keshav.state}\n")
"""


# Write a class "calculator" capable of finding sqaure, cube and square root of a number.
"""Q-2
from math import sqrt

n=int(input("Enter number for square: "))
class calculator:
  square= n*n
  
number=calculator()
print(number.square)

n2=int(input("Enter number for square root: "))
number.sqrt=n2=sqrt(n2)
print(number.sqrt)

n3=int(input("Enter number for cube: "))
number.cube=n3*n3*n3
print(number.cube)
"""

#Create a class with a class attribute a; create an object from it and set'a' directly using object.a=o. Does this change the class attribute?
"""Q-3"""
class demo:
  a= 4

o =demo()
print(o.a)   # prints the class attribute because no instance attribute set there
o.a = 0    # instance attribute set
print(o.a)  # prints the instance attribute

print(demo.a) # no class attribute doesn't change 

# Add a static method in problem 2, to greet the user with hello 
"""Q-4"""
class calculator:
  def __init__(self,n):
    self.n=n

  def square(self):
    print(f"The square is {self.n*self.n}")
  def cube(self):
    print(f"The cube is {self.n*self.n*self.n}")
  def sqaureroot(self):
    print(f"The square root is {self.n**1/2}")
  @staticmethod
  def greet():
    print("Hello, good morning😊 ")

a=calculator(4)
a.greet()
a.square()
a.sqaureroot()
a.cube()

# write a class train which has methods to booka a ticket, get status(no of seats) and get fare information of train running under indain Railways.
"""Q-5"""
from random import randint
class Train:
  def __init__(self, TrainNo):
    self.TrainNo=TrainNo

  def book(self, fro, to):
    print(f"Ticket is booked in train no:{self.TrainNo} from  {fro} to {to}")

  def getstatus(self):
    print(f" Train no:{self.TrainNo} is running onn time...") 

  def getFare(self, fro, to):
    print(f"Train fare of train no:{self.TrainNo} from{fro} to {to} is Rs. {randint (222, 2000)}")


T=Train(123355)
T.book("Gwalior"," Delhi")
T.getFare("Gwalior"," Delhi")
T.getstatus()


# Can you change the self parameter inside a class to something else( say"harry"). Try changing "slf" or "harry" and see the effects.

"""Q-6 """
# nothing would happen
class calculator:
  def __init__(slf,n):
    slf.n=n
# see, nothing will happen, it work fine.
  def square(harry):
    print(f"The square is {harry.n*harry.n}") 
  def cube(self):
    print(f"The cube is {self.n*self.n*self.n}")
  def sqaureroot(self):
    print(f"The square root is {self.n**1/2}")
  @staticmethod
  def greet():
    print("Hello, good morning😊 ")

a=calculator(4)
a.greet()
a.square()
a.sqaureroot()
a.cube()

