import random

"""
1 = Rock
0= paper
-1 = scissiors

"""


# The simple version 
"""
computer = random.choice([-1, 0 , 1])
roc_paper_scissior= { "r" : 1, "p" : 0, "s" : -1 }

i=0
while True:
  In=input("enter your choice:") 
  print("\n")

  if In in roc_paper_scissior:
    break
  elif i==0:
    print("We are playing rock paper scissors bro 😄!")
    print("let's do this again!!\n")
    i+=1
  elif i==1:
    print("Brooo 😵‍💫 seriously? Focus! Try again...")  
    i+=1
  
  elif i==2:
    print("I'm done with you, Iam not playing 😤")
    exit() 

you=roc_paper_scissior[In]

reverse_dic = { 1 : "Rock 🪨", 0 : "Paper 📃", -1 : "scissiors ✂️"}
print(f"You choose {reverse_dic[you]}\n \t& \nComputer choose {reverse_dic[computer]}\n")

if(computer == you):
  print("it's a draw\n")

else:
  if(computer == 1 and you == -1):
    print(" computer win!!💀\n ")

  elif(computer == -1 and you == 0):
    print(" computer win!!💀\n ")

  elif(computer == 0 and you == 1):
    print("computer WIN!!💀\n ")

  elif(computer == 1 and you == 0):
    print("You WIN!!🎉\n ")

  elif(computer == 0 and you == -1):
    print(" You WIN!!🎉\n ")

  elif(computer == -1  and you == 1):
    print(" You WIN!!🎉\n ")

  else:
    print("something went wrong\n")

"""



# we can same do with finding a pattern in the conditions statements and 
# make it more efficent and can save big lines if code--

"""
# if((computer - you) == -1 or (computer - you)== -2):
#     print(" computer win!!💀")

# else:
#    print("You WIN!!🎉")
"""


# the final version of the game is this --


with open("hi-score.txt") as f:
  hi_score=f.read()
if(hi_score!=""):
  hi_score = int(hi_score)
else:
  hi_score = 0

def game():
 
 scores = {"User": 0, "computer": 0}
 while True:
 
  computer = random.choice([-1, 0 , 1])
  roc_paper_scissior= { "r" : 1, "p" : 0, "s" : -1 }



  i=0
  while True:
    In=input("enter your choice:") 
    print("\n")

    if In in roc_paper_scissior:
      break
    elif i==0:
      print("We are playing rock paper scissors bro 😄!")
      print("let's do this again!!\n")
      i+=1
    elif i==1:
      print("Brooo 😵‍💫 seriously? Focus! Try again...")  
      i+=1
    
    elif i==2:
      print("I'm done with you, Iam not playing 😤")
      exit() 

  you=roc_paper_scissior[In]

  reverse_dic = { 1 : "Rock 🪨", 0 : "Paper 📃", -1 : "scissiors ✂️"}
  print(f"You choose {reverse_dic[you]}\n \t& \nComputer choose {reverse_dic[computer]}\n")

  
  if(computer == you):
    print("it's a draw\n")

  else:
    if((computer - you) == -1 or (computer - you)== 2):
      print(" computer win!!💀")
      scores["computer"] +=1
    else:
      print("You WIN!!🎉")
      scores["User"] +=1

    
    
  print(f"Current Score -->>  Computer score: {scores['computer']}  🆚 Your score : {scores['User'] } ")

  if scores["User"] > scores["computer"]:
    with open("hi-score.txt", "w") as f:
     f.write(str(scores["User"]))
     print(f"\n🎉 New High Score! Your score: {scores['User']}")
  else:
   print(f"\nYour Score: {scores['User']} | High Score: {hi_score}")


    # want to play again
  play_again = input("Play again? (y/n): ")
  if play_again != "y":
    break


print("Staring the game....")
game()
