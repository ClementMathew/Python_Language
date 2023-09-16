
def summation(lower,upper) :
    if lower>upper:
        return 0
    
    else:
        return lower+summation(lower+1,upper)

print(summation(1,10))