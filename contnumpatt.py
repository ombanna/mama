# Continue Numm Pattern

n = int(input("How Manay Pattern You Want To Print\n"))

def contnumpatt(n):
    num = 1
    for i in range(0, n):
        for j in range(0, i + 1):
            print(num, end=" ")
            num = num + 1
        print("\r")
contnumpatt(n)

