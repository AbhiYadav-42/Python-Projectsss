# Tuple = 
a=(1,33,54,765,11,2,24," hAAry","AKASH",True) 
# This is tuple, it is just like the List but the diiference is that it is unmutable means we cannot change the existing value of the tuple 

#Methods of tuple
# *rememberr just like the strings , the tuples too create a new tuples when we apply methods in it because we cant change into the existing one. 

count=a.count(765)  #it will count that element that, how  many times it is in there. 
print(count) #output: 1

length=print(len(a)) #output: 10

index=a.index(2) # it will find that at which index that element is stored 
print(index) #output: 5

tuple0=(1,2)
tuple1=(3,)
concatenation= tuple1 + tuple0  # It is called concatenation , it is represented by -->>  +
print(concatenation)  #output: (3,1,2)


print(2 in tuple0) # it is called Membership , it is represented by -->>  in
#output: True

repeatiton= print(tuple1*5)# it is called repeatition , it will make the elmenets repeat it is representes by -->> *
#output: (3,3,3,3,3)

h1,h2=tuple0  # it wil l assign/unpack into the individual Variables.
print(h1,h2) #OUTPUT: 1 2

"""
Abhi ,hARRY = a     
print(Abhi, hARRY,) #errror because you need to give the variabled to each and every element present in the Tuple
"""

