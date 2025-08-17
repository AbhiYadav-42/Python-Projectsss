#Write  a program to print the muliplaction table of given number using FOR LOOP.
"""Q-1"""
I=int(input("Enter the number:"))

for i in range(0,11):
  print(f"{I} x {i} = {I*i}")


# write a program to greet all the person names  stored in a list 'l' and which starts with S.
"""Q-2"""
l=["harry", "Soham","Sachin", "Rahul", "ajay" ]

for i in l:
  if(i.startswith("S")):
   print(f"Good morning  :{i}")
  
  else:
    print("......")

# print the muliplication table using WHILE LOOP
"""Q-3"""
N=int(input("Enter the number:"))

i=1
while(i<11):
  
  print(f"{N} x {i} = {N *i}")
  i = i+1



#Write a program to find whether a given number is prime or not

"""Q-4"""
n=int(input("Enter number: "))

for i in range(2,n):
  if(n%i )==0:
    print(f"{n} is not prime")
    break
  else:
    print(f"{n} is  a prime number")
    break

# write a program to find the sum of first ten natural number
"""Q-5"""
n=int(input("enter : "))
i = 1
sum=0
while(i<=n):
  sum += i
  i += 1
print(sum)


""" Tried with FOR LOOP"""
sum=0
for i in range (1,11):
  sum+=i
print(sum)

# write a program to calculate  the factorial of a given number using for loop 

"""Q-6"""
n = (int(input("enter: ")))
fac=1
for i in range(1, n+1):
 fac *= i 
print(f"The factorial of {n} is {fac}") 


""" Tried with while loop"""
n=int(input("enter: "))
i=1
fac=1
while(i<=n):
  fac *= i
  i+=1
print(f"The factorial of {n} is {fac}") 



# Write a program to print the following star pattern
"""
  *
 ***
*****  for n=3
"""

"""Q-7"""
n =int(input("enter the n: "))

for i in range(1,n+1):
  print(" "* (n-i), end="")
  print("*"* (2*i-1), end="")
  print("")



#  Write a program to print the following star pattern
"""
for n=3
*
**  
***
"""

"""Q-8"""
n= int(input("Enter n: "))

for i in range(1,n+1):
  print( "*" * i ) 



#  Write a program to print the following star pattern
"""
for n=3
***
* *  
***

"""
"""Q-9"""
n= int(input("enter:"))

for i in range(1, n+1):
  print("*"*(n))
  print("*",end="")
  print(" "* (n-2),end="")          #I did it,
  print("*" )                   # but not in the correct way
  print("*" * n)
  break


""" Correct way to do"""
n= int(input("enter: " ))

for i in range(1, n+1):
  if(i==1 or i==n):
    print("*" * n, end="")
  else:
    print("*",end="")
    print(" " *(n-2), end="")
    print("*", end="")
  print("")



# write a program to print the multiplication table in reverse order
"""Q-10"""
I=int(input("Enter the number:"))

for i in range(1,11):
  print(f"{I} x {11-i} = {I*(11-i)}")


