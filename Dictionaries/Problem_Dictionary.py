# 1. Assume that the variable data refers to the dictionary {'b':20, 'a':35}.
# Write the values of the following expressions:
# a. data['a']
# b. data.get('c', None)
# c. len(data)
# d. data.keys()
# e. data.values()
# f. data.pop('b')
# g. data # After the pop above

# 2. Assume that the variable data refers to the dictionary {'b':20, 'a':35}.
# Write the expressions that perform the following tasks:
# a. Replace the value at the key 'b' in data with that value's negation.
# b. Add the key/value pair 'c':40 to data.
# c. Remove the value at key 'b' in data, safely.
# d. Print the keys in data in alphabetical order.

data = {'b': 20, 'a': 35}

print(data['a'])
print(data.get('c', None))
print(len(data))
print(data.keys())
print(data.values())
print(data.pop('b'))

data['b'] = -data['b']
data['c'] = 40
data.pop('b', None)

for key in sorted(data.keys()):
    print(key)
