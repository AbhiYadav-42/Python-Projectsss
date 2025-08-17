# Create a class 2-D vector and use it to create another class representing a 3-D vector
"""Q-1"""
class TwoDvector:
  def __init__(self, i ,j):
    self.i = i
    self.j = j

  def show(self):
    print(f"The vector is {self.i}i + {self.j}j")

class ThreeDvector(TwoDvector):
  def __init__(self,i,j,k):
    super().__init__(i,j)
    self.k = k

  def show(self):
    print(f"The vector is {self.i}i + {self.j}j + {self.k}k")

p= input("Enter i: ")
k= input("Enter j: ")
a=TwoDvector(p,k)

a.show()
c=int(input("Enter k: "))
b=ThreeDvector(p,k,c)
b.show()

# Create a class 'Pets' from a class 'Animals' and further create a class 'Dog' from 'Pets'. Add a method 'Bark' to class 'Dog'

class Animals:
  pass

class Pets(Animals):
    pass

class Dog(Pets):
  def __init__(self, bark):
    self. bark = bark
  print("Bouw BOuw!!")    

# Create a class 'Employee'  and salary and increment properties to it   
"""Q-3"""
class Employee:
  salary = 1200000
  increment = 15000

a= Employee()


# Write a method 'salaryAfterIncrement' method with a @property decorator with a setter which changes the value of increment based on the salary
"""Q-4"""
class Employee:
  def __init__(self, salary, increment):
    self.salary = salary
    self.increment = increment 

  @property 
  def salaryAfterIncrement(self ):
    return (self.salary +self.salary *(self.increment/100))
     

  @salaryAfterIncrement.setter
  def salaryAfterIncrement (self, new_salary):
    self. increment = ((new_salary/self.salary)-1) * 100

salary=int(input("Enter:"))
increment=int(input("Enter: "))
a= Employee(salary, increment)

print(f"{a.salaryAfterIncrement}")
print(a.increment)

new=int(input("Enter: "))


# Write a class 'complex' to represent complex numbers, along with overloaded operators '+' and '*' which adds and multiplies them

class complex():
  def __init__(self,real, img):
    self.real = real
    self.img= img

  def __add__(self,c2):
    return complex(self.real + c2.real, self.img + c2.img )
  
  def __mul__(self,c2):
    return complex(self.real * c2.real - self.img * c2.img , self.real *c2.img + self.img * c2.real )  
  
  def __str__(self):
    return f"{self.real} + {self.img}i"
  

# c1 = complex(1,2)
# c2 = complex(3,4)
# print(c1 + c2 )
# print(c1 * c2)
# print(c1)
c1 = int(input("Enter real part: "))
c2 = int(input("Enter imaginary part : "))

c3 = int(input("Enter real part : "))
c4 = int(input("Enter imaginary part: "))

comp1 = complex(c1, c2)
comp2 = complex(c3, c4)

add_result = comp1 + comp2
mul_result = comp1 * comp2

print(f"Complex number \nAddition = {add_result} \nMultiplication = {mul_result}")


# 
"""Q-5"""
class vector:
  def __init__(self,x,y,z):
    self.x=x
    self.y=y
    self.z=z

  def __add__(self,other):
    result =vector(self.x + other.x, self.y +other.y , self.z + other.z)
    return result 
  
  def __mul__(self,other):
    result = self.x * other.x + self.y * other.y + self.z * other.z
    return result
  
  def __str__(self):
    return f"Vector({self.x}i, {self.y}j, {self.z}k)"
  
v1 = vector(1 ,2,3)
v2 = vector(4 ,5,6)
v3 = vector(7 ,8,9)

print(v1+v2)  #
print(v1+v2)

print(v1+v3)
print(v1+v3)


#  Write __str__() method to print the vector as follows:
#   7i +8j +10k
# assume vector of dimension 3 for this problem
"""Q-6"""
class vector:
  def __init__(self,x,y,z):
    self.x=x
    self.y=y
    self.z=z

  def __add__(self,other):
    result =vector(self.x + other.x, self.y +other.y , self.z + other.z)
    return result 
  
  def __mul__(self,other):
    result = self.x * other.x + self.y * other.y + self.z * other.z
    return result
  
  def __str__(self):
    return f"Vector({self.x}i +  {self.y}j + {self.z}k)"
  
v1 = vector(1 ,2,3)
v2 = vector(4 ,5,6)
v3 = vector(7 ,8,9)

print(v1 + v2)  #
print(v1 * v2)

print(v1 + v3)
print(v1 * v3)

# 
"""Q-7"""
class vector:
  def __init__(self,l):
    self.l = l

  def __len__(self):
    return len(self.l)


v1 = vector ( [ 1, 2, 3 ] ) 
print(f"length of this vector :  {len(v1)}")