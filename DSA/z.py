#practice
# import array as arr
# from array import *
# a=arr.array('i',[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17])
# a=array('i',[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17])
# print(a)
# print(a[3])
# print(a[8])
# print(a[11])
# print(a[12])
# print(a[-1])
# print(a)

# print(a[-13])
# print(a[-8])
# print(a[-3])

# print(len(a))
# # print(a)

# a.append(18)
# print(a)
# a.extend([19,20])
# print(a)
# a.insert(4,0)
# print(a)

# print(a.pop())

# a.remove(11)
# print(a)

# b=array('i',[21,22,23,24])
# c=array('i',[])
# c=a+b
# print(c)

# print(np.Concatenate[a,b])

# slicing, reversing
# print(a[0:4])
# print(a[0:15])
# print(a[::-1])

# copy
# print(a[0].data)
# q=a.copy()
# print(q)


#practice
# import numpy as np
# a=np.array([1,2,3,4,5,6,7])
# b=np.array([[10,20,30],[40,50,60],[70,80,90]])
# c=np.array([[[1,2,3],[4,5,6]],[[5,3,8],[9,7,2]]])
# q=np.array([[2,3,4],[7,4,9],[5,0,2]])
# print(a)
# print(b)
# print(c)

# print("dtype-",a.dtype)
# print("ndim-",c.ndim)
# print("shape-",c.shape)
# print("size-",b.size)
# print("flatten-",c.flatten())
# print("reshape-",b.reshape(3,3))
# print("reshape-",c.reshape(6,2))
# print("transpose-",np.transpose(b))
# print("diagonal-",np.diag(b))
# print("slice-",b[0:2])
# print("specific",b[2,2])
# # print(b.dot(q))
# d=np.array(np.arange(2,13))
# print(d)

# print("multiply-",b.dot(q))

# print("sort",np.sort(q))
# # np.sort(ascending=False)==np.sort(q)

# print(np.concatenate((b,q)))
# print(np.concat([a,d]))

#practice
# a.append(18)
# print(a)
# a.extend([19,20,21,22])
# print(a)
# a.insert(3,18)
# print(a)
# a.remove(11)
# print(a)
# print(a.pop())

# p=array('i',[62,84,40])
# r=array('i',[222,88,44])
# s=array('i',[])
# s=a+p+r
# print(s)
# print(len(s))
# print(a[9])


#practice
# def create_array():
#     array=[]
#     length=int(input("length-"))
#     for i in range(length):
#         element=int(input("element-"))
#         array.append(element)
#     return array
# print(create_array())


# practice
# import numpy as np
# a=np.array([[1,2,3],[5,7,8],[3,7,2]])
# print(a)

# print(a.dtype)
# print(np.linalg.matrix_rank(a))
# print(a.shape)
# print(a.size)
# print(a.flatten())

# f=np.array([[1,9,2],[4,8,3],[22,11,3]])

# print(np.concatenate((a,f)))
# print(np.concat([a,f]))
# print(a.dot(f))
# print(np.subtract(a,f))
# print(np.sum([a,f]))


# queue
# practise
# using list
"""queue=[]
def enqueue():
    n=int(input("enter head element: "))
    if len(queue)==0:
        print("stack is empty")
        queue.insert(0,n)
    else:
        queue.append(n)
        print(queue)

def dequeue():
    if len(queue)==0:
        print("queue is underflow")
    else:
        queue.remove(queue[0])
        print(queue)

def display():
    if len(queue)==0:
        print("queue is empty")
    else:
        print("last element: ", queue[0]," ", "first element",queue[-1])
while(True):
    print("enter your option: ","1.enqueue,2.dequeue,3.display,4.exit")
    option=int(input("enter your option: "))

    if option==1:
        enqueue()
    elif option==2:
        dequeue()
    elif option==3:
        display()
    elif option==4:
        exit()
        break"""


# using LL
"""
class queue:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class queue_LL:
    def __init__(self):
        self.head=None
        self.tail=None
        
    def enqueue(self,data):
        n=queue(data)
        
        if self.head is None:
            self.head=n
            self.tail=n
        else:
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            temp.next=n
            
    def dequeue(self):
        if self.head is None:
            print("queue is empty")
        else:
            self.head=self.head.next
            
    def display(self):
        if self.head is None:
            print("queue is empty")
        else:
            temp=self.head
            while temp is not None:
                print(temp.data,end="-->")
                temp=temp.next
            print("none")
            
            
mylist=queue_LL()
mylist.enqueue(30)
mylist.enqueue(20)
mylist.enqueue(10)
mylist.display()
mylist.dequeue()
mylist.display()
print()
"""

# stack
# practise
#using list
"""
stack=[]
def push():
    n=int(input("enter top element: "))
    if len(stack)==0:
        print("stack is empty")
        stack.insert(0,n)
    else:
        stack.append(n)
        print(stack)
    
def pop():
    if len(stack)==0:
        print("stack underflow")
    else:
        stack.pop()
        print(stack)
    
def display():
    if len(stack)==0:
        print("stack is empty")
    else:
        print("last element",stack[-1]," ","first element",stack[0])
        
while(True):
    print("select from this given options: ","1.push,2.pop,3.display,4.exit")
    option=int(input("select your option: "))
    
    if option==1:
        push()
    elif option==2:
        pop()
    elif option==3:
        display()
    elif option==4:
        exit()
        break"""



# using LL
"""class stack:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class stack_ll:
    def __init__(self):
        self.top=None
        self.bottom=None
    
    def push(self,data):
        n=stack(data)
        
        if self.top is None:
            self.top=n
            self.bottom=n
        else:
            temp=self.top
            while temp.next is not None:
                temp=temp.next
            temp.next=n
            
    def pop(self):
        if self.top is None:
            print("stack underflow")
        else:
            self.top.next.next.next=None
            
    def display(self):
        if self.top is None:
            print("stack is empty")
        else:
            temp=self.top
            while temp is not None:
                print(temp.data,end="-->")
                temp=temp.next
            print("none")


mylist=stack_ll()
mylist.push(12)
mylist.push(13)
mylist.push(14)
mylist.push(15)
mylist.display()
mylist.pop()
mylist.display()
print()
"""

# practise
#recurssion
"""def printN(n):
    if n>0:       #base case
        printN(n-1)        #recursive case
        print(n,end=" ")
# printN(10)

def printNeven(n):
    if n>0:
        printNeven(n-1)
        print(2*n,end=" ")
# printNeven(10)

def printNodd(n):
    if n<=0:
        return None
    return printNodd(n-1),print(2*n-1,end=" ")
        # printNodd(n-1)
        # print(2*n-1,end=" ")
# printNodd(10)

def sumN(n):
    if n==1:
        return 1
    return n+sumN(n-1)
print(sumN(5))

def sumNeven(n):
    if n==1:
        return 2
    return 2*n+sumNeven(n-1)
print(sumNeven(5))

def sumNodd(n):
    if n==1:
        return 1
    return 2*n-1+sumNodd(n-1)
print(sumNodd(5))

def sumNsquare(n):
    if n==1:
        return 1
    return n*n+sumNsquare(n-1)
print(sumNsquare(5))

# using recursive
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
print(fact(5))

# using tail recursive
def tfact(n,a=1):
    if n==0:
        return a
    return tfact(n-1,n*a)
print(tfact(5))

# using recursive
def fib(n):
    if n==0:
        return 0
    if n==1:
        return 0
    if n==2:
        return 1
    else:
        return (n-1)+(n-2)
print(fib(6))

# using tail recursive
def fib(n,a=0,b=1):
    if n==0:
        return a
    if n==1:
        return b
    else:
        return fib(n-1,b,a+b)
print(fib(6))
"""

# practise
# linked-list
"""class node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
        
class sll:
    def __init__(self,start=None):
        self.start=start
        
    def is_empty(self):
        return self.start==None
        
    def at_start(self,data):
        n=node(data,self.start)
        self.start=n
        
    def at_end(self,data):
        n=node(data)
        if not self.is_empty():
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp.next=n
        else:
            self.start=n
            
    def search(self,data):
        temp=self.start
        while temp is not None:
            if temp.item==data:
                return temp
            temp=temp.next
        return None
    
    def insert_after(self,temp,data):
        if temp is not None:
            n=node(data,temp.next)
            temp.next=n
            
            
    def display(self):
        temp=self.start
        while temp is not None:
            print(temp.item,end="-->")
            temp=temp.next
        print("none")
        
    def del_start(self):
        if self.start is not None:
            self.start=self.start.next
            
    def del_end(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start=None
        else:
            temp=self.start
            while temp.next.next is not None:
                temp=temp.next
            temp.next=None
            
    def del_any(self,data):
        if self.start is None:
            pass
        elif self.start.next is None:
            if self.start.item==data:
                self.start=None
        else:
            temp=self.start
            while temp is not None:
                if temp.next.item==data:
                    temp.next=temp.next.next
                    break
                temp=temp.next
                
s=sll()
s.at_start(10)
s.at_start(20)
s.at_start(30)
s.at_start(40)
s.display()
s.at_end(12)
s.display()
s.insert_after(s.search(30),55)
s.display()
print()

s.del_start()
s.display()
s.del_end()
s.display()
s.del_any(55)
s.display()
print()"""

#DLL
class node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next
        
class DLL:
    def __init__(self,start=None):
        self.start=start
        
    def is_empty(self):
        return self.start==None
    
    def at_start(self,data):
        n=node(None,data,self.start)
        if not self.is_empty():
            self.start.prev=n
        self.start=n
        
    def at_end(self,data):
        temp=self.start
        while temp.next is not None:
            temp=temp.next
        n=node(temp,data,None)
        temp.next=n
        
    def search(self,data):
        temp=self.start
        while temp.next is not None:
            if temp.item==data:
                return temp
            temp=temp.next
        return None
    
    def at_any(self,temp,data):
        if temp is not None:
            n=node(temp,data,temp.next)
            temp.next=n
        
    def display(self):
        temp=self.start
        while temp is not None:
            print(temp.item,end="<-->")
            temp=temp.next
        print("none")
        
    def del_start(self):
        if self.start is not None:
            self.start=self.start.next
            
    def del_end(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start=None
        else:
            temp=self.start
            while temp.next.next is not None:
                temp=temp.next
            temp.prev.next=None
            

        
    def del_any(self,data):
        if self.start is None:
            pass
        # elif self.start.next is None:
        #     if self.start.item==data:
        #         self.start=None
        else:
            temp=self.start
            while temp is not None:
                if temp.item==data:
                    if temp.next is not None:
                        temp.next.prev=temp.prev
                    else:
                        # temp.prev is not None:
                        temp.prev.next=temp.next
                temp=temp.next
                
        
s=DLL()
s.at_start(12)
s.at_start(14)
s.at_start(17)
s.at_start(19)
s.display()
s.at_end(45)
s.display()
s.at_any(s.search(14),56)
s.display()
print()

s.del_start()
s.display()
s.del_end()
s.display()
s.del_any(17)
s.display()
print()


