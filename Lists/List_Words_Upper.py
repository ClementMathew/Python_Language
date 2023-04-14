sentence = "This example has five words."

words = sentence.split()
print(words)

for index in range(len(words)):
    words[index] = words[index].upper()

print(words)