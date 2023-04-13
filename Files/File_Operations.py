# Absolute Pathname

f = open("/Programming/Python_Programs/Files/test.txt","w")
f.write("Hello")
f.close()

# Relative Pathname

f1 = open("Files/test.txt","r")
s= f1.read()
print(s)

# Relative Parent Pathname

f2= open("../test2.txt","w")
f2.write("Clement")
f2.close()

# Operations

import os

print(os.path.exists("/Programming/Python_Programs/Files/test.txt"))

print(os.path.isdir("/Programming/Python_Programs/Files"))
print(os.path.isdir("/Programming/Python_Programs/Files/test.txt"))

print(os.path.isfile("/Programming/Python_Programs/Files"))
print(os.path.isfile("/Programming/Python_Programs/Files/test.txt"))

print(os.path.getsize("/Programming/Python_Programs/Files"))

print(os.path.isfile("/Programming/Python_Programs/Files"))

print(os.path.normcase("/Programming/Python_Programs/Files"))

print(os.chdir("/Programming/Python_Programs/Files"))

print(os.getcwd())

print(os.listdir("/Programming/Python_Programs/Files"))

print(os.mkdir("/Programming/Python_Programs/Files/test"))

print(os.rmdir("/Programming/Python_Programs/Files/test"))

# create rempve.txt in module2
#print(os.remove("remove.txt"))

print(os.rename("remove.txt","rename.txt"))
