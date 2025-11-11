


import time
import random
logo = """
  _    _ _       _                 _                            
 | |  | (_)     | |               | |                           
 | |__| |_  __ _| |__   ___ _ __  | |     _____      _____ _ __ 
 |  __  | |/ _` | '_ \ / _ \ '__| | |    / _ \ \ /\ / / _ \ '__|
 | |  | | | (_| | | | |  __/ |    | |___| (_) \ V  V /  __/ |   
 |_|  |_|_|\__, |_| |_|\___|_|    |______\___/ \_/\_/ \___|_|   
            __/ |                                               
           |___/                                                
"""

while True:
  print("\033[95m")  # Purple color
  print(logo)
  print("\033[0m")    # Reset color
  time.sleep(1)
  Q1= [{
    "name": "Virat Kohli",
    "desc": "Cricketer 🏏",
    "value": 273}, # in millions

    {
    "name": "Tylor swift",
    "desc": "Singer 🎤",
    "value" : 281 # millions
  }] 


  q2=[
    {
      "name": "Bat-man",
      "desc": "Vigilante 🦇",
      "value": 70 
    },
    {
      "name": "Spider-man",
      "desc": "Friendly neighbourhood 🕷️",
      "value": 95
    }]

  q3=[{
    "name": "GTA V",
    "desc": "Open-world game 🎮",
    "value": 10 #millions
  },
  {
    "name": "Call of Duty: Warzone",
    "desc": "Battle royale shooter 🔫",
    "value": 70 #millions
  }]


  q4 = [{
    "name": "Avatar",
    "desc": "by James Cameron - Sci-fi (2009) 🌌",
    "value": 2.92 #billion
  },
  {
    "name": "Avengers: Endgame",
    "desc": "by Marvel Studios - Super-hero  (2019) 🦸‍♂️",
    "value": 2.80 #billion
  }]


  def play_q1():
    print("\n")
    print("Computer choosing...")    
    print("\n")
    time.sleep(2)
    n1,n2 = random.sample(Q1,2)
    print("Who has more instagram followers?? ")

    print("🅰️", n1["name"], "-", n1["desc"])
    print("🅱️", n2["name"], "-", n2["desc"])

    Type = input("Type 'A' or 'B'-> 🎯 ")

    if (Type == "A"):
      _1choice = n1 
      _2choice = n2
    else:
      _1choice = n2
      _2choice = n1

    if (_1choice["value"] > _2choice["value"]):
      print("✅ correct!! 🎉")

      print(f" {n1["name"]} = {_1choice["value"]} millions \n{n2["name"]} = {_2choice["value"]} millions")

      return True
    
    else:
      print("❌ wrong!! 😢")  
      print(f" {n1["name"]} = {_1choice["value"]} millions \n{n2["name"]} = {_2choice["value"]} millions")

      return False
  



  def play_q2():
    print("\n")    
    print("Computer choosing...")  
    print("\n")      
    time.sleep(2)  

    n1,n2 = random.sample(q2,2)
    print("Who has more online searches? 🔍")

    print("🅰️", n1["name"], "-", n1["desc"])
    print("🅱️", n2["name"], "-", n2["desc"])

    Type = input("Type 'A' or 'B'-> 🎯 ")

    if (Type == "A"):
      _1choice = n1
      _2choice = n2
    else:
      _1choice = n2
      _2choice = n1

    if (_1choice["value"] > _2choice["value"]):
      print("✅ correct!! 🎉")
      print(f" {n1["name"]} = {_1choice["value"]} millions \n{n2["name"]} = {_2choice["value"]} millions")

      return True
    
    else:
      print("❌ wrong!! 😢")

      print(f" {n1["name"]} = {_1choice["value"]} millions \n{n2["name"]} = {_2choice["value"]} millions")      
      return False
 

  def play_q3():
    print("\n")    
    print("Computer choosing...") 
    print("\n")  
    time.sleep(2)

    n1,n2 = random.sample(q3,2)
    print("Which game had more Active players in 2024?? 🎮 ")

    print("🅰️", n1["name"], "-", n1["desc"])
    print("🅱️", n2["name"], "-", n2["desc"])

    Type = input("Type 'A' or 'B'-> 🎯 ")

    if (Type == "A"):
      _1choice = n1
      _2choice = n2
    else:
      _1choice = n2
      _2choice = n1

    if (_1choice["value"] > _2choice["value"]):
      print("✅ correct!! 🎉")
      print(f" {n1["name"]} = {_1choice["value"]} millions \n{n2["name"]} = {_2choice["value"]} millions")

      return True
    else:
      print("❌ wrong!! 😢")
      print(f" {n1["name"]} = {_1choice["value"]} millions \n{n2["name"]} = {_2choice["value"]} millions")                                                                 
      return False 


  def play_q4():
    print("\n")    
    print("Computer choosing...")    
    print("\n")    
    time.sleep(2)   
    n1,n2 = random.sample(q4,2)
    print("Which movie made more money at the box office?? 🎬🤑")

    print("🅰️", n1["name"], "-", n1["desc"])
    print("🅱️", n2["name"], "-", n2["desc"])

    Type = input("Type 'A' or 'B'-> 🎯 ")

    if (Type == "A"):
      _1choice = n1
      _2choice = n2
    else:
      _1choice = n2
      _2choice = n1
     
    if (_1choice["value"] > _2choice["value"]):
      print("✅ correct!! 🎉")
      print(f" ${n1["name"]} = {_1choice["value"]} billions \n${n2["name"]} = {_2choice["value"]} billions")

      return True
    
    else:
      print("❌ wrong!! 😢")
      print(f" ${n1["name"]} = {_1choice["value"]} billions \n${n2["name"]} = {_2choice["value"]} billions")

      return False


  questions = [play_q1, play_q2, play_q3, play_q4]
  random.shuffle(questions)
  
  for q in questions:
    result =q()
    if result == False:
      break
  

  if(result == True):   
    print("\n")
    time.sleep(1)
    print("And...") 
    print("\n") 
    time.sleep(1)
    print("You...")
    print("\n")
    time.sleep(2)
    print("🏆 You answered all correctly!")  
    print("\033[33m")  # Set text color to yellow (gyold)
    print(r"""
           ___________
          '._==_==_=_.' 
          .-\:      /-. 
         | (|:.     |) | 
          '-|:.     |-' 
            \::.    / 
             '::. .' 
               ) ( 
             _.' '._ 
            `"""""""`
         🏆 CHAMPION 🏆""")
    print("\033[0m")  # Reset to default color



    # want to play again
  play_again = input("Play again? (y/n): ")
  if play_again != "y":
    break
