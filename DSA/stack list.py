"""stack=list()
def push():
    n=int(input("enter number: "))
    if len(stack)==0:
        print("stack is empty")
        stack.insert(0,n)
    else:
        stack.append(n)
        
def pop():
    if len(stack)==0:
        print("stack underflow")
        
    else:
        stack.pop()
        
def display():
    if len(stack)==0:
        print("stack is empty")
    else:
        print(stack)
        
while(True):
    print("select option","1.push, 2.push, 3.display. 4.exit")
    option=int(input("enter option: "))
    if option==1:
        push()
    if option==2:
        pop()
    if option==3:
        display()
        break"""
    # else:
    #     print("not available")
        
        
        
class stack:
    def __init__(self):
        self.n=[]
        
    def is_empty(self):
        return len(self.n)==0
    
    def push(self,data):
        # if not self.is_empty():
        self.n.append(data)
        # else:
        #     raise IndexError("stack is empty")
        
    def pop(self):
        if not self.is_empty():
            return self.n.pop()
        else:
            raise IndexError("stack is empty")
        
    def peek(self):
        if not self.is_empty():
            return self.n[-1]
        else:
            raise IndexError("stack is empty")
        
    def size(self):
        return len(self.n)
    
    def display(self):
        if not self.is_empty():
            print(self.n)
        else:
            return IndexError("stack is empty")
        
s1=stack()
s1.push(10)
s1.push(20)
s1.push(30)
s1.push(40)
s1.display()
print(s1.size())
s1.pop()
s1.display()
print(s1.size())
print(s1.peek())
s1.display()
print()


"""#stack by Inhereting list class
class stack(list):
    def is_empty(self):
        return len(self)==0

    def push(self,data):
        self.append(data)
        
    def pop(self):
        if not self.is_empty():
            return super().pop()
        else:
            raise IndexError("stack is empty")
        
    def peek(self):
        print(self[-1])
    
    def size(self):
        print(len(self))
    
    # def insert(self,index,data):
    #     raise AttributeError("insert not possible")
    
    def display(self):
        if not self.is_empty():
            print(self)
        else:
            raise IndexError("stack is empty")
s1=stack()
s1.push(10)
s1.push(20)
s1.push(30)
s1.push(40)
s1.size()
s1.peek()
s1.display()
s1.pop()
s1.size()
s1.peek()
s1.display()
print()
"""
