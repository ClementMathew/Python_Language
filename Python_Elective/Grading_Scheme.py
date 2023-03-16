mark = int(input("Enter the mark : "))

if(mark > 89):
    print("Grade A")

elif(mark<90 and mark>79):
    print("Grade B")

elif(mark<80 and mark>69):
    print("Grade C")

else:
    print("Grade F")