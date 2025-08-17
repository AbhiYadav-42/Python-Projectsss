# BREAK--->> It is used to come out of the loop when encountered. it instructs the program to exit the loop now.

for i in range(25):
  if(i==20):
    break   # The moment i==20 it stops exectuing and exit the loop..
  print(i)


# CONTINUE--->> It is used to stop the current iteration of the loop and conitune with the next one. it instructs the Program to "skip this iteration"

for i in range(35):
  if(i==5 and i ==20):  # The moment i becomes 5 or 20  it skips..
    continue
  print(i)


#PASS --->> It is a null statement in python. 
  # PASS statement instructs to "do nothing.."

 # PASS statemnet be like--> eat five star and "do nothing" 🤣

l=[7,8,9,10]
for i in range(4):
  print(l[i])
  pass

i=0
while(i<len(l)):
  print(l[i])
  i+=1