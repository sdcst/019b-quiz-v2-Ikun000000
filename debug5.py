#!python3
"""
Fix this program.
It should ask the user to enter in 10 numbers and see
if the number is positive or negative
"""
for i in range(1,11):
 a=float(input("Numbers"))
 if a > 0:
  print("that is a positive number")
 elif a < 0:
  print("that is a negative number")
 elif a==0:
  print("Zero")