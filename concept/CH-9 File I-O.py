#                  Chapter -9 file I/O
# The random- access memory is volatile, and all its contents are lost once a program terminates in order to persist the data fprever, we use files.

# A file is data stored in a storage  device. A python program can talk to the file by reading content from it and writing content to it 


"""
_____________________________________   Write    __________
|                                   |------>>>   |        |
|Computer program written in python |<<-----     |  FILE  |
|___________________________________|   Read     |________| 

"""

# Types of files.
"""
 1. Text files (.txt , .c , .py....etc)
 2. Binary files(.jpg , .dat...etc)

 Python has a lot of funciton for reading, updating, and deleting files
  """


#        READ files in PYTHON

f= open("file.txt")  # opens the file in the read mode
data = f.read()  # read its contents 
print(data)    # Print its content
f.close()     # close the file 


#       Write files in PYTHON

st="I love U too"
file=open("file2.txt", "w") # for writing u need to enter "w"
file.write(st)
file.close()



#        READLINE FUNCITON

f=open("file2.txt")


# lines = f.readlines() # it is use to read one full line at a time
# This function prints in the list form

line1 = f.readline()
print(line1, type(line1))

line2=f.readline()
print(line2,type(line2))

line3=f.readline()
print(line3, type(line3) )

line4= f.readline()
print(line4, type(line4) )

line5=f.readline()
print(line5=="")  # This shows that, Yes it is inside empty string 

f.close()


# READLINE() using WHILE LOOP
f= open("file.txt")
line=f.readline()
while(line!=""):
  print(line)
  line =f.readline()

f.close()

#       Modes of Opening a file
"""
r --->> Open for Reading
w --->> Open for Writing
a --->> Open for Appending
+ --->> Open for Updating
rb -->> Will open for read in binary mode
rt -->> Will open for read in text mode
"""


#       WITH Statement
# OPEN the file in read mode using 'with', which automatically closes the file

with open("thistext") as f:
  text= f.read()
print(text)# print the content