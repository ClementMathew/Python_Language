
# Selection

n1 = int(input("Enter the 1st number : "))
n2 = int(input("Enter the 2nd number : "))
n3 = int(input("Enter the 3rd number : "))

if (n1<n2 and n3<n2):
    print("Maximum = ",n2)

elif (n2<n1 and n3<n1):
    print("Maximum = ",n1)
    
else:
    print("Maximum = ",n3)