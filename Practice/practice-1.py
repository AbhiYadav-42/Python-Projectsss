""" Q-1"""
#Write a program to print the "Twinkle-Twikle little star" Poem in python.
print("Poem-->")
print('''
Twinkle Twinkle, Little Star
How I wonder what you are
Up above the world so high
Like a diamond in the sky
Twinkle Twinkle Little Star
How I wonder what you are!
      
Twinkle Twinkle, Little Star
How I wonder what you are
Up above the world so high
Like a diamond in the sky
Twinkle Twinkle Little Star
How I wonder what you are! ''' )


"""Q-2"""
# Install an external module and use it to perform an operation of your interst #

import pyttsx3
engine = pyttsx3.init()
engine.say(" What the fFFFFFFFFFFFFFFuUUUUUUUUUUUUUUUUUUUKKKKKKKKKKKKKK !!")
engine.runAndWait()


"""Q-3"""
#write a python to print the contents of a directory using OS module Search Online for the function which does that.
import os

# Specify the directory path (use '.' for current directory)
directory_path = 'D:\\Sekiro.SDT.GOTY.v1.06\Sekiro.SDT.GOTY.v1.06'

# List all files and directories in the specified path
try:
    contents = os.listdir(directory_path)
    print(f"Contents of '{directory_path}':")
    for item in contents:
        print(item)
except FileNotFoundError:
    print(f"The directory '{directory_path}' was not found.")
except PermissionError:
    print(f"Permission denied to access '{directory_path}'.")



