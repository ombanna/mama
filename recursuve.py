#RECURSION FUNCTION
 #FACTORIAL
# n!= n * (n-1) * (n-2) * (n-3) *.......1
# n!= n * (n-1)!

def factorial_iterative(n):
    fac = 1
    for i in range(n):
        fac = fac * (i+1)
    return fac
def factorial_recursive(n):

    if n==1:
        return 1
    else:
        return  n * factorial_recursive(n-1)
def febonacci(n):
    if n<0:
        print("Invalid Input!!!")
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return febonacci(n-1) + febonacci(n-2)
num = int(input("Enter A Number For Factorial,Febonacci \n"))
print("factorial Usung Iterative Number Is : ", factorial_iterative(num))
print("factorial Usung Recursive Number Is : ", factorial_recursive(num))
print("Febonacci  Number Is : ", febonacci(num))

"""
#FEBONACCI SERIES
# 0 1 1 2 3 5 8 13 21
def febonacci(n):
    if n<0:
        print("Invalid Input!!!")
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return febonacci(n-1) + febonacci(n-2)

num = int(input("Enter Number:\n"))
print(febonacci(num))



"""






# def febonacci(n):
#
#     if n==0:
#         return 0
#     else:
#         return n + febonacci(n-1)
#
#
#
# num = int(input("Enter A Number For Febonacci \n"))
# print("Fibonacci Number Is : ", febonacci(num))