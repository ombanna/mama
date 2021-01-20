"""
def triangle(n):
    # number of spaces
    k = 2 * n - 2

    # outer loop to handle number of rows
    for i in range(0, n):

        # inner loop to handle number spaces
        # values changing acc. to requirement
        for j in range(0, k):
            print(end=" ")

            # decrementing k after each loop
        k = k - 1

        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0, i + 1):
            # printing stars
            print("* ", end="")

            # ending line after each row
        print("\r")

    # Driver Code


n = 5
triangle(n)
"""
n = int(input("How Many Number You Want To Print Pattern\n"))
def triangel(n):
    k = 2 * n -2

    for i in range(0,n):
        for j in range(0,k):
            print(end=" ")
        k = k -1
        for j in range(0,i + 1):
            print("*",end=" ")
        print("\r")
triangel(n)



n = int(input("Enter The Number Of Pattern Want To Print\n"))

def tr(n):
    k = 2 * n - 2
    for i in range(0,n):
        for j in range(0,k):
            print(end=" ")

        k = k -1
        for  j in range(0,i + 1):
            print("*", end=" ")
        print("\r")
tr(n)


















