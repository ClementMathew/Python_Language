#

def displayRange(lower,upper):
    while lower<=upper:
        print(lower)
        lower = lower+1

displayRange(10,15)

# Recursive

def displayRangeRec(lower,upper):
    if lower<=upper:
        print(lower)
        displayRangeRec(lower+1,upper)

displayRangeRec(16,20)