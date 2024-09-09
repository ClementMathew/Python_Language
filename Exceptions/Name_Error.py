
def fun(a):

    # throws NameError because 'b' is not defined properly
    print("Value of b:", b)

try:
    fun(5)

except NameError:
    print("NameError Occurred and Handled")
