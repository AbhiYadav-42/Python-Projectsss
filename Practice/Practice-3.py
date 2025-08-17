#Write a program to display a user enters name followed by Good Afternoon using the input() function.
"""Q-1
A=input("Enter the sir's name: ")
B=input("Enter the madam's name:")
print(f"Good Afternoon Mr. {A} and Mrs. {B}")
""" 

#Write a program to fill in a letter given below with name and date
"""Q-2
letter = '''
        Dear<|Name|>,
        You are selected!
        <|Date|>
        '''

print(letter.replace("<|Name|>","Harry").replace("<|Date|","24 Sept 2020."))
"""
#Write a program to detect double space in a string.
"""Q-3
name=" Harry is a good  boy "
print(name.find("  "))
"""

#Write a program to replace the double spaces in the Q-3 to single space
"""Q4
name = " Harry is a good  boy "
print(name.replace("  "," "))
"""

# * Strings are imutuable which that you cannot change them by running function on them

#Write a program to format the following letter using escape sequence
"""
letter="Dear Harry,\n \t This Python course is nice\nThanks!! "

print(letter)
"""