# Write a program to find the greatest of three numbers using the fucniton
"""Q-1"""

def gratest(a, b ,c):
  if(a>b and a>c):
   return print(f"{a} is the greatest")
  elif(b>a  and  b>c):
   return print(f"{b} is the greatest")
  elif(c>a and c>b):
   return print(f"{c} is the greatest")

a= int(input("enter A: "))
b= int(input("enter B: "))
c= int(input("enter C: "))
print(f"{gratest(a, b, c)}")



# Write a program to convert the celsius to fahrenheit
"""Q-2"""
def temperature(f):

  return 5 * ( f - 32 ) / 9

f=int(input("enter the temperature in f:"))
print(f"{round(temperature(f), 2) } \N{DEGREE SIGN}C")


#write a recrusive funciton to print the sum of the frist ten natural numbers 
"""
sum(1) = 1
sum(2) = 1 + 2 
sum(3) = 1 + 2 + 3
sum(4) = 1 + 2 + 3 + 4 
sum(n) = 1 + 2 + 3 + 4.......n-1 + n

# so we can write like this 
  sum(n) = sum(n-1) + n
"""
"""Q-3"""
def sum(n):
  if(n==1):
    return 1
  return sum(n-1) + n

n=int(input("Enter the number: "))
print(sum(n))


# Write a python funciton to print the pattern 
"""
for n=3
***
**
*
"""

""" Q-4"""
def pattern(n):
  if(n==0):
    return
  print("*"*n,)
  pattern(n-1)

n=int(input("Enter: "))
pattern(n)


# Write a program to convert inches to cms.
"""Q-5"""
def inch_to_cm(inch):
  return inch*2.54

n=int(input("Enter value in inches: "))
print(f"{n} inches in cm is {inch_to_cm(n)}")



# Write a python funciton to remove a word from the list and strip at same time 
"""Q-6"""
def rem(l, word):
  n=[]
  for item in l:
    if not(item==word):
      n.append(item.strip(word))
      return n
l= ["harry", "shubhan", "Rohan", "Abhya"]
print(rem(l, "an"))

#

"""Q-7"""
def table(n):
  for i in range(1,11):
    print(f"{n} x {i} = {n*i}")
  return "\n"
n=int(input("Enter : "))
print(table(n))
