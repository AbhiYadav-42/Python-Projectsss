friends=["Apple", "Orange",3,3.3443,"Akash",False]
# As you can see we can store any value of any datatype in a List.

#List can be indexed just like strings.
friends[0] #Apple 
friends[4] # Akash
# friends[70] #error
friends[1:3] #[orange ,3] List slicing. This is same just like the Strings.


"""
 As we know, 
 Strings are unmutuable 
 but List are mutuable
example,
"""

friends[0]="Grapes"
print(friends[0])
                  # Grapes

# List Methods
L1=[9,6,75,54,312,8,1,0,3,2]

L1.sort() #it will sort the element in ascending order 

L1.append("") #it will insert at last , if i run apppend empty["append()"] it shows an error 

L1.insert(1, 466) #it will insert 466 at index of 1 , first index then the element youu want to insert in the list

L1.pop() 
print(L1)


L1.reverse() #it will reverse the order of the list 
L1.remove(8) #it will remove the particular element fromt the list

                  
