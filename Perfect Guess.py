import random
import time
while True: 
  # Difficulty selection
  level= input("Choose the difficulty level: ").lower()
  if level ==  "easy":
    n = random.randint(1,10)
    print("guess between: 0 to 10 ")
  elif level == "medium":
    n= random.randint(1,50)
  elif level == "hard":
    n = random.randint(1,100)

  else:
    print("Invalid ")
    n= random.randint(1,10)    


  tries = 0
  print("computer choosing....")
  time.sleep(1.5)         # added the delay of 2 secs .
  print("computer had choosen the number...")
  time.sleep(1)

  i = 0
  while True:       # Guessing loop
    guess= int(input("Guess the number: "))
    
    # attempt counter
    tries+=1
    if tries == 5:
        print("This one's gonna be tougher, I can feel it 😏")
        
    if (guess == n):
      print(f"It took {tries} tries to guess")
      if tries == 1:
        print("Are you a mind reader!?😲") 
      elif tries == 2 or tries == 3:
       print("""
sharp shooter 🤠

\033[95m⣼⠛⠒⠶⠤⣄⣀⡀\033[0m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\033[95m⠉⢹⡗⠒⠦⢤⣄⣉⠙⠓⠲⠤⣤⣀⡀\033[0m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\033[95m⠀⠈⠉⠙⠓⠶⠤⣬⣉⡛⠒⠶⠤⣄⣉⡉⠛⠲⠦⠤⣄⣀\033[0m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀\033[92m⠈⠉⠙⠓⠲⠦⢬⣉⣙⠒⠲⠤⣄⣈⡉⠙⠒⠶⣤⣄⣀⡀\033[0m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\033[96m⠈⠉⠛⠒⠦⢤⣍⣙⠓⢺⠉⣖⠒⠭⣝⡓⠲⠤⣤⣶\033[0m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\033[93m⠈⠙⠳⠦⠤⣌⣉⡉⠀⠀⢠⡞⣿⣦⡀\033[0m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\033[94m⠈⠙⣿⣿⣿⢧⣙⣍⢧⣀⣀⣀⡀\033[0m⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠁⠀\033[91m⢹⡄⢿⡛⠷⡢⢍⡓⢤⣀\033[0m⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\033[91m⠙⠓⠿⣟⠈⠳⣌⠑⢌⢙⡶⣤⡀\033[0m⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\033[90m⠈⠳⣄⠈⠢⡀⣑⢍⠢⡉⢻\033[0m
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\033[90m⠈⠳⣆⠈⠪⡚⠠⣡⢿\033[0m
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\033[90m⠈⠳⣄⣀⡴⠋\033[0m
""")
      elif tries >=7:
        print("Persistent soul💪")
      elif tries == 4 or tries == 6:
       print("Average Joe 🙂")

      break
    
    if(guess == n ):
      print("🎯")
      break
    else:
      if(guess < n):
        print("⬆️")
        
      else:
        print("⬇️")
        

    # want to play again
  play_again = input("Play again? (y/n): ")
  if play_again != "y":
    break
  i +=1










   