# Absolute Pathname

f = open("/Computer_Programming/Python_Programs/Python_Elective/Module_2/test.txt","w")
f.write("Hello")
f.close()

# Relative Pathname

f1 = open("Python_Elective/Module_2/test.txt","r")
s= f1.read()
print(s)

# Relative Parent Pathname

f2= open("../test2.txt","w")
f2.write("Clement")
f2.close()

# Operations

import os

print(os.path.exists("/Computer_Programming/Python_Programs/Python_Elective/Module_2/test.txt"))

print(os.path.isdir("/Computer_Programming/Python_Programs/Python_Elective/Module_2"))
print(os.path.isdir("/Computer_Programming/Python_Programs/Python_Elective/Module_2/test.txt"))

print(os.path.isfile("/Computer_Programming/Python_Programs/Python_Elective/Module_2"))
print(os.path.isfile("/Computer_Programming/Python_Programs/Python_Elective/Module_2/test.txt"))

print(os.path.getsize("/Computer_Programming/Python_Programs/Python_Elective/Module_2"))

print(os.path.isfile("/Computer_Programming/Python_Programs/Python_Elective/Module_2"))

print(os.path.normcase("/Computer_Programming/Python_Programs/Python_Elective/Module_2"))

print(os.chdir("/Computer_Programming/Python_Programs/Python_Elective/Module_2"))

print(os.getcwd())

print(os.listdir("/Computer_Programming/Python_Programs/Python_Elective/Module_2"))

print(os.mkdir("/Computer_Programming/Python_Programs/Python_Elective/Module_2/test"))

print(os.rmdir("/Computer_Programming/Python_Programs/Python_Elective/Module_2/test"))

# create rempve.txt in module2
#print(os.remove("remove.txt"))

print(os.rename("remove.txt","rename.txt"))
