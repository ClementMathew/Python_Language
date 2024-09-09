
def fun(a):

    if a == 3:
        # throws ZeroDivisionError for a == 3
        b = a / (a - 3)
    else:
        b = 3
        print("Value of b :",b)

try:
    fun(4)
    fun(3)

# note that parentheses () are necessary here for multiple exceptions
except ZeroDivisionError:
    print("ZeroDivisionError Occurred and Handled")
