def wrapper(f):
    def fun(l):
        # complete the function
        
        front = "+91"
        
        ls = []
        
        for i in range(len(l)):
            numinit = l[i]
            ls.append(numinit[-10:]) 
        
        ls.sort()
        
        for i in range(len(ls)):
            num = ls[i]
            first = num[-10:-5]
            second = num[-5:]
            print(front,first,second)
            
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input("Enter phone number : ") for _ in range(int(input("Enter number of phone : ")))]
    sort_phone(l) 