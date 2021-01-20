# pyramid

n = int(input("How Manay Pattern You Want To Print\n"))
def pyramidpatt(n):
    for i in range(0,n):
        for j in range(0,i + 1):
            print("*", end=" ")
        print("\r")
pyramidpatt(n)
