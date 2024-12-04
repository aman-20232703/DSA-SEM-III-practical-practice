"""
def printN(n):
    if n>0:
        printN(n-1)
        print(n,end=" ")
        
def printNreverse(n):
    if n>0:
        print(n,end=" ")
        printNreverse(n-1)
        
def printNOdd(n):
    if n>0:
        printNOdd(n-1)
        print(2*n-1,end=" ")
        
def printNeven(n):
    if n>0:
        printNeven(n-1)
        print(2*n,end=" ")
        
def printNOddreverse(n):
    if n>0:
        print(2*n-1,end=" ")
        printNOddreverse(n-1)
        
def printNevenreverse(n):
    if n>0:
        print(2*n,end=" ")
        printNevenreverse(n-1)
        
printN(10)
printNreverse(10)
printNOdd(10)
printNeven(10)
printNOddreverse(10)
printNevenreverse(10)
"""


"""
def sumM(n):
    if n==0:
        return 0
    return n+sumM(n-1)

def sumModd(n):
    if n==0:
        return 0
    return 2*n-1+sumModd(n-1)

def sumMeven(n):
    if n==1:
        return 2
    return 2*n+sumMeven(n-1)

def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)

def square(n):
    if n==0:
        return 1
    return n*n+square(n-1)


print("sum is",sumM(5))
print("sum is",sumModd(10))
print("sum is",sumMeven(10))
print("sum is",fact(5))
print("sum is",square(5))
"""

def fact(n,a=1):
    if n==0:
        return a
    else:
        return fact(n-1,n*a)
    
print(fact(5))

def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return (n-1)+(n-2)

print(fib(6))


def fib(n,a=0,b=1):
    if n==0:
        return a
    elif n==1:
        return b
    else:
        return fib(n-1,b,a+b)
    
print(fib(6))