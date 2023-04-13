s = "Python rules!"

print("List of words : ")
print(s.split())

print("\nTo Uppercase : ")
print(s.upper())

print("\nPosition of rules : ")
print(s.find('rules'))

print("\nReplace ! with ? : ")
print(s.replace("!", "?"))

print(s.endswith('i'))
print('totally'.join(s.split()))