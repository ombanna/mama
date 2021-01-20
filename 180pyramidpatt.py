# 180 pyramidd Pattern Printing

n = int(input("How Many Number You Want To Print Pattern\n"))
def pyramidpatt(n):
    k = 2 * n -2

    for i in range(0,n):
        for j in range(0,k):
            print(end=" ")
        k = k -2
        for j in range(0,i + 1):
            print("*",end=" ")
        print("\r")
pyramidpatt(n)
