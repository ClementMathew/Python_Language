# first method

info = {}

info["Name"] = "Sandy"
info["Occupation"] = "Hacker"

for key in info:
    print(key,info[key])

print()

# second method

grades = {90:"A",80:"B",70:"C"}

print(list(grades.items()))

print()

# third method

for (key,value) in grades.items():
    print(key,value)