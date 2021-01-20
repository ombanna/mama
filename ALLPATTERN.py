# PATTERN
#THIS IS FIRST PROGRAM

print("How Many Number You Want To Print Pattern\n""Enter A Number\n",)
n= int(input())
def pattern(n):

    for i in range (0, n):
        for j in range (0,i+1):
            print(" * " ,end=" ")
        print("\r")

# pattern(n)

#THIS IS SECOND PROGRAM

# print("How Many Number You Want To Print Pattern\n""Enter A Number\n",)
#  n= int(input())
#  def pattern(n):
    for i in range (n,-1,-1):
        for j in range (0,i+1):
            print(" * " ,end=" ")
        print("\r")
 # pattern(n)

#THIS IS THIRD PROGRAM

# print("How Many Number You Want To Print Pattern\n""Enter A Number\n",)
# n= int(input())
#  def pattern(n):
    k=2*n-2
    for i in range (0,n):
        for j in range (0,k):
            print(end=" ")
        k = k - 1
        for j in range(0,i+1):
            print(" * ",end=" ")
        print("\r")
# pattern(n)



# print("How Many Number You Want To Print Pattern\n""Enter A Number\n",)
# n= int(input())
# def pattern(n):
    k=2*n-2
    for i in range (n,-1,-1):
        for j in range (k,0,-1):
            print(end=" ")
        k = k + 1
        for j in range(0,i+1):
            print(" * ",end=" ")
        print("\r")
pattern(n)



"""
print("How Many Number You Want To Print Pattern\n""Enter A Number\n",)
n= int(input())
def pattern(n):

    for i in range (0, n):
        for j in range (0,i+1):
            print(" * " ,end=" ")
        print("\r")
# for i in range(n,-1,-1):
#     for j in range(0, i + 1):
#         print(" * ", end=" ")
#     print("\r")

pattern(n)



"""