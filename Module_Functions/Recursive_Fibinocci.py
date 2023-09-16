
def fibinocci(n):
    if n<3 :
        return 1
    
    else:
        return fibinocci(n-1) + fibinocci(n-2)

print(fibinocci(1))
print(fibinocci(2))
print(fibinocci(3))
print(fibinocci(4))
print(fibinocci(5))