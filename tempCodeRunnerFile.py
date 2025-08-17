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
# Abhi.name="Abhi Yadav"
Abhi.greet()
Abhi.get()
