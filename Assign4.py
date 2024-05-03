#!python3
"""
Billy is inviting people to his party.  He is accepting requests
from his friends, but only wants to send 1 invitation out per
person. He decides to store names in a list, and only add the
ones that are not already there.  Can you help a brother out?

Your program should keep asking the user to enter in a name 
(first and last).  If the name is not on the list, add it,
otherwise say "That name is already on the list".

if the user enters in a blank line, then stop the input.
Sort the list of names (it will be sorted by first name)
and print out all of the names on the list.  Also print out
the number of names on the list so he knows how many 
invitations to send.

This program will require you to incorporate everything we
have learned so far.
"""
name=[]
a=0
for i in range(1,1001):
    x = input("Friends' name")
    if x in name:
        print("That name is already on the list")
    elif x == "":
        name.sort()
        print(name)
        print(f"You have invited {a} people")
        break
    else:
        name.append(x)
        a+=1
