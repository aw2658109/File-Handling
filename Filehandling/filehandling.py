# File handling in python for read data:
# R Mode:
f=open("demo.txt","rt")
data=f.read()
print(data)
print(type(data))
f.close()
# READLINE:
#Second Example:
print("second example:")
f=open("demo.txt","rt")
line1=f.readline()
print(line1)

print("second example:")
f=open("demo.txt","rt")
line2=f.readline()
print(line2)

# Write data in file as W MODE and a MODE as for append data means add:
f=open("demo.txt","a")
f.write("\n i am learn BS DATA SCIENCE From air university islamabad:")
f.close()
f=open("wahab.txt","w")
f.close()
#R+ MODE:
f=open("wahab.txt","r+")
f.write("hello ")
print(f.read())
f.close()
#W+ MODE:
f=open("wahab.txt","w+")
print(f.read())
f.write("My favorite player fakar zaman:")
f.close()
# A+ MODE:
f=open("wahab.txt","a+")
print(f.read())
f.write("code with harry:")

#With syntax Read:
with open("sample.txt","r") as f:
    print(f.read())
#with syntax write data:
with open("sample.txt", "w") as f:
        f.write("NEW DATA")
# Deleting File in python:
import os
os.remove("sample.txt")



