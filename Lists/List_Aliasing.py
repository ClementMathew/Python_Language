first = [10,20,30]

second = first

print(first)
print(second)
print()

first[1] = 99

print(first)
print(second)
print()

# prevent aliasing side effects

third = []

for element in first:
    third.append(element)

print(first)
print(third)
print()

first[1] = 100

print(first)
print(third)
print()

# another method

fourth = list(first)
print(first)
print(fourth)
print()

first[1] =101

print(first)
print(fourth)
print()

# to check aliases

print(first == second) # but it returns true if contents is same

print(first is second)