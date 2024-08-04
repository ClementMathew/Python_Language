grades = {90:'A',80:'B',70:'C'}

print("Display in Key's Sorted Order")

theKeys = list(grades.keys())
theKeys.sort()

for key in theKeys:
    print(key,grades[key])