
n = int(input("How Manay Pattern You Want To Print\n"))

def alphabet(n):
    num = 65
    for i in range(0, n):
        for j in range(0, i + 1):
            ch = chr(num)
            print(ch, end=" ")
        num = num + 1
        print("\r")
alphabet(n)



n = int(input("How Manay Pattern You Want To Print\n"))

def alphabet(n):
    num = 65
    for i in range(0, n):
        for j in range(0, i + 1):
            ch = chr(num)
            print(ch, end=" ")
            num = num + 1
        print("\r")
alphabet(n)
