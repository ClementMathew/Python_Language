# Odd numbers from range 1 to 10

odd_square = [x ** 2 for x in range(1,11) if x %2 == 1]

print(odd_square)

# same as

odd_square_ = []

for x in range(1,11):
    if x%2 ==1:
        odd_square_.append(x**2)

print(odd_square_)