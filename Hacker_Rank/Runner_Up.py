if __name__ == '__main__':
    n = int(input("Enter the number of entry : "))
    arr = map(int, input("Enter the numbers : ").split())

li= []
runner = []
li = list(arr)
li.sort()
for i in li:
    if(max(li) != i):
        runner.append(i)
runner.sort()
print(max(runner))
