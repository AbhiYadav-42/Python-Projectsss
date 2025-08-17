#Set--> A set in Python is a built-in data type that represents an unordered collection of unique elements

#Property of Set
"""
1. It is unordered,
2. it is unique, becuase eliminates the duplicated values,
3. It is immutbale in natute,
4. It is unindexed,
5. and It uses the mathematical operations 
    like-
    a). Differences
    b). Union
    c). Interesection
    d). Symmetric differences
    e). mirrorring 
"""

s0={1,2,3,4,55,5,5,5,5,7,7,7,7,7}
# print(s0)     #OUTOUT : {1, 2, 3, 4, 5, 55, 7}

s={}# it is a empty set

s1=() # This is an empty set

# Set Methods;
set={1,4,23,.34,5,5,6,8,8,8,}

set.add(3)  # Adds the element in the set. if it there only then it do nothing

set.remove(8) # removes the specific Element you want from the set


# set.clear() # it make the set empty , clear out all the elements

newset=set.copy() # Returns the shallow copy of the set
print(newset)         #[ OUTPUT:                 ]
print(set)           # [ {0.34, 1, 3, 4, 5, 6, 23} ] 

# union
s9={1,3,4,78,56}
s10={2,4,5,1,56}

print(s9.union(s10))
print(s10.intersection(s9))
          

sets={"harry", [1,2,4]}
print(sets)