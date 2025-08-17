#  Inheritance is a way of creating a new class from an existing class.


#Types of  INHERITANCE
#     > Single inheritance
#     > Multiple inheritance
#     > Mulilevel inheritance



# Single Inheritance
"""
Single inheritance occurs when child class inherits only a single parent class 
____________
|          |
|  Base    |
|__________|
   |
 \ | /
__\_/_______
|         |
| Derived | 
|_________|
""" 

# syntax:

class employee:              # Base class
  pass                      #code 

class Programmer(employee):       #Derived or child class
  pass                            #code

"""
Here, it means we can use the attributes of 'employee' in ' Programmer' object.
      Also, if we try to change in the employee it will automatically change in the Programmer object 
"""


#                Multiple INHERITANCE
# -> Mulitple inheritance occurs when the child class inherits from more than one parent classes 
"""
   _____________       ______________
  |             |     |              |
  |  Parent1    |     |  Parent2     |
  |_____________|     |______________|
          \              /
           \            /
            \          /
           __\________/__
          |             |
          |   Child     |
          |_____________|
"""

class Parent1:
    com="ww"
    def method1(self):
      print("Method from Parent1")

class Parent2:
    lang="hin"
    def method2(self):
      print("Method from Parent2")

class Child(Parent1, Parent2):
    name="ab"
    def child_method(self):
      print(f"Method from Child {self.com} {self.lang} {self.name}")

# Example usage:
c = Child()
c.method1()        # From Parent1
c.method2()        # From Parent2
c.child_method()   # From Child

# we can call parent 1 and parent 2 from the child 

#               Multilevel INHERITANCE
# When a child becomes a parent for another child class.
"""
   _____________
  |             |
  |   Parent    |
  |_____________|
         |
         v
   _______________
  |               |
  | Child 1       |
  |_______________|
         |
         v
   ______________
  |              |
  |  Child 2     |
  |______________|
"""
class Employee:
   a=1

class programmer(Employee):
   b=2

class Manger(programmer):
   c=3

o = Employee()
print(o.a)        # Prints the a attribute     

o = programmer()    # Prints the a and b attribute
print(o.a, o.b)

o=Manger()            #Prints the a, b and c attribute
print(o.a, o.b, o.c)



#                 SUPER() method
# super() method is used to access the methods of a super class in the derived class
class Employee:
   def __init__(self):
      print("constructor of employee")
      a =1 

class Manager(Employee):
   def __init__(self):
    super().__init__()  
# super() calls the parent class constructor 
    print("Constructor of manager")
   c=3
      #__init__ calls constructor of the base class  

m= Manager()


#                  Class method
# This method is a method which is bound to the class and not the object of the class.

class Employee:
   a=1
# Here, This decorator let u use the orignal value of the attribute no the changed one    
   @classmethod
   def show(cls):
    print(f"The class attribute of a is {cls.a}")
e=Employee()
e.a=42

e.show()
# Class method let you directly us the class attributes ignoring the change made by the object or instance attribute.


#              Property decorator
class Employ:
   @property
   def name(self):
      print("Abhi")
      return f"{self.harf} {self.harL}"
   
   @name.setter
   def name(self,value):
      self.harf=value.split(" ")[0]
      self.harL=value.split(" ")[1]
e=Employ()
e.name = "harry putter"      #Setter is triggered  
print(e.name)                # Getter is triggered
# @property decorator is also called getter method



#Operator overloading
# Operation in pyhton can be overloaded using dunder methods or magic methods
""""""
# p1.__add__(p2)
# p1.__sub__(p2)
# p1.__mul__(p2)
# p1.__truediv__(p2)
# p1.__floordiv__(p2)
"""
__str__()"""      
   #used to set what gets displayed upon calling str(obj)
"""
__len_() """
    #Used to set what gets displayed upon calling __len__() or len(obj)
class Number:
   def __init__(self,n):
      self.n = n

   def __add__(self, num):
      return self.n + num.n
   
n=Number(1)
m=Number(2)

print(n + m)