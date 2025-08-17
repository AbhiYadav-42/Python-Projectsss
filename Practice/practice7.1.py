# Print first 10 natural numbers using while loop

i=1
while(i<11):
  print(i)
  i+=1


#Print the following pattern 
"""
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5
"""
n=int(input("Enter: "))

for i in range(1,n+1):
  for j in range(1,i+1):
    print(j,end='')
  
  print("")


# Calculate sum of all numbers from 1 to a given number
def sum(n):
  i=1
  s=0
  a=0
  while(i<n+1):
    s=s+i
    i+=1
    a=s/n
  return s,a


n=int(input("enter: "))
s,a=sum(n)
print(f"Sum is {s}")
print(f"Average is {a}")
