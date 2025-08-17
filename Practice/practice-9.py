# Write a program to read the text from a given file 'poems.txt' and find whether it contains the word "twinkle"
"""Q-1"""
f=open("Poems.txt")
twinkle=f.read()
if("twinkle"in twinkle):
  print("twinkle present in the poem")
else:
  print("twinkle present in the poem")
f.close()


# The game() fucniton in program let a user play a game and returns the score as an integer. You need to read a file HI-score.txt which is either blank or contains the previous HI-SOCRE. You need to write a program to update the HI-socre whenever the game() fucniton  breaks the HI-Score.
"""Q-2
import random

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

"""

""" 
import random

def game():
  print("ypu are playing the game..")
  score= random.randint(1,65)

  # Fetch the hiscore

  with open("H-score.txt") as f :
   hiscore = f.read()
   if(hiscore!=""):
     hiscore=int(hiscore)
   else:
     hiscore=0

  print(f"Your score: {score}")
  if(score>hiscore):

    #write this hiscore to the file
    with open("H-score.txt","w") as f:
      f.write(str(score))
  return score
     
game()
""" 

# Write a program to gernate multiplacation tables from 2 to 20 and write to the differnt files. place these files in a folder for a 13- year old child 
"""Q-3"""
def gernate_table(n):
  table=""
  for i in range(1,11):
    table+= f"{n} x {i} = {n*i}\n"

  with open(f"Tables/table_{n}", "w") as f:
    f.write(table)


for i in range(2, 21):
  gernate_table(i)


# A file contains a word "Donkey" multiple times. You need to write a program to replace this word with ###### by updating the same file
"""Q-4"""
with open("Donkeey.txt") as f:
  content=f.read()

  update=content.replace("donkey","####")

  with open("Donkeey.txt", "w") as f:
    f.write(update)
  
print(content)
 

# Repeat program 4 for a list of such words to be censored.
"""Q-5"""

censored_words = [
    "fuck", "sexy","bitch", "boobs", "ass", "dick", "shit", "cunt",
    "porn", "sex", "nude", "xxx", "escort",
    "kill", "murder", "shoot", "bomb", "stab",
    "weed", "cocaine", "meth", "heroin"
]


def censor(text, censored_words):
  for word in censored_words:
    text=text.replace(word, "*" *len(word))
  return text

with open("abusive.txt") as f:
  content = f.read()

# update = censor(content,censored_words)
for word in censored_words:
  content = content.replace(word, "*" *len(word))

with open("abusive.txt","w") as f:
  f.write(content)

print(content)

# Write a program to mine a log file and finf dout whether it contains'python'

"""Q-6"""

with open("log.txt") as f:
  line=f.read()

if("python"  in line or "Python" in line or "PYTHON" in line or "pythonn" in line ):
  print("Yes, python is present")
else:
  print("No, python is not present")  


# Write a program to find out the line number where python is present from Q-6
"""Q-7"""

with open("log.txt") as f:
  lines=f.readlines()

lineno =1
for line in lines:
  if("python"  in line or "Python" in line or "PYTHON" in line or "pythonn" in line ):
    print(f"Yes, python is present. Line no:{lineno}")
    break
  lineno +=1

else:
  print("No, python is not present") 


# Write a program to make a copy of text file "this.text"
"""Q-8

with open("this.txt")as f:
  content=f.read()

  with open("this_copy.text","w")as f:
    f.write(content)
"""

# Write a program to find out whether a file is identical & matches the content of another file
"""Q-9"""
with open("this.txt")as f:
 content=f.read()

with open("this_copy.text","r")as f:
 content1 =f.read()

 if(content==content1):
  print(" Yes, the contents are identical")
 else:
  print("No, content  are not identical")
  

# Write a program to wipe out the content of a file using python
"""Q-10
with open("hi-score.txt","w")as f:
  f.write("")
"""

# Write a python program to rename a file to renamed_by_python.txt
"""Q-11"""

import os
with open("python.txt")as f:
  content= f.read()

with open("renamed_by_python.txt","w")as f:
   f.write(content)

os.remove("python.txt")

