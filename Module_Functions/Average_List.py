
lyst = [5,10,10]

def average(lyst):
    theSum = 0

    for number in lyst:
        theSum += number
    
    return theSum/len(lyst)

print(average(lyst))