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