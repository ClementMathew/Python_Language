
# # Solution of a Third Degree Polynomial (Another Method)

A =int(input('Enter the coefficient of x^2: '))
B =int(input('Enter the coefficient of x: '))
C =int(input('Enter the constant: '))

D=(B**2)-(4*A*C)
Sol1 = (-B -(D**0.5))/(2*A)
Sol2 = (-B +(D**0.5))/(2*A)
print("The solutions are {:.2f} and {:.2f}".format(Sol1,Sol2))