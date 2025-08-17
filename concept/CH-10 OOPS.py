# Solving a problem by creating is one of the most popular approches in programming.THis is called aboject-oriented programming (OOPS)

#             CLASS
# A class is a blueprint for creating object


#             OBJECT
# Object is an instantiation of class. When class is defined, a template(info) is defined. Memory is allocated only after instantiation

# Modelling A probelm in OOPS
"""
  Noun-> class-> Employee
  Adjective-> Attributes->name, age, salary
  Verbs-> Methods->getsalary(), increment()
"""

#               Class Atrributes
# An attribute that belongs to the class rather than a particular object

class Employee:       #Class name 
  language= "py"      #This is an Class attribute
  salary = 120000

harry=Employee()                        #Object Instatiation
harry.name = "Harry"                    # This is an Instance attribute
Employee.language = "python"            # changing class Attribute
print(harry.name, harry.language, harry.salary)


ABHI=Employee()
ABHI.name ="Abhi"
ABHI.language = " Javascript"
 # *Instance attributes, take preference over class atrributes files during assignment & retrieval.
 
print(ABHI.name, ABHI.language, ABHI.salary)

# Here name is object or Instance attribute and slaray and langauge are atrributes as they directly belong to the class 




#               Self parameter
# Self refers to the instance of the class. It is automatically passed with a fucniton call form an object.
class Employees:
  language= "Javascript"
  salary =150000
  name='Abhi'

  def get(self):   
    print(f"The name of the Employee is {self.name}\n The language is{self.language}\nThe Salary  {self.salary} ")

     # Rememberr to put self(can use other name ) in your funciton, if you not it will not work 

  

     # What if? we want to use the fucntion without the self ,then what?
     # we can use the Static Method , 
# Like this👇
  @staticmethod    
  def greet():            
    print("Good morning")  



Abhi=Employees()
Abhi.name="Abhi Yadav"
Abhi.greet()
Abhi.get()

#         __INIT__() CONSTRUCTOR
"""
 It is a special method which is first run as soon as the object is created, 

 It takes self-argument and can also take further arguments... 

"""

#  like this 👇
class greet:
  def __init__(self):
    print("Good morning")  
#It will automatically prints, it works on the principal of self call 
greet()
f= greet()

            # final example 
class Employer:
  def __init__(self, name ,Language,  salary):
    self.name=name
    self.language=Language
    self.salary=salary
  print("The employer description 👇\n ")

Abhi = Employer("Abhi","Python","160000" )      
print(f"The name of the Employer is {Abhi.name}\n Master in Language -> { Abhi.language} \nSalary -> { Abhi.salary}")