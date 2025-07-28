#coundown timer usinf for loops

import time

my_time =int(input("Enter time in seconds: "))

for x in range(my_time, 0,-1):
  seconds = x % 60
  minutes = int(x/60)
  hour    = int(x/3600)
  print(f"{hour:02}:{minutes:02}:{seconds:02}")
  time.sleep(1)


print("Time is up!")