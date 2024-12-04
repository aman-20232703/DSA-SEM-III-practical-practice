
class node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
        
class stack:
    def __init__(self):
        self.top=None
        self.data_count=0
        
    def is_empty(self):
        return self.top==None
    
    def push(self,data):
        n=node(data,self.top)
        self.top=n
        self.data_count+=1
        
    def pop(self):
        if not self.is_empty():
            data=self.top.data
            self.top=self.top.next
            self.data_count-=1
            return data
        else:
            raise IndexError("stack is empty")
        
    def peek(self):
        if not self.is_empty():
            return self.top.data
        else:
            raise IndexError("stack is empty")
        
    def size(self):
        return self.data_count
    
    
    def display(self):
        if not self.is_empty():
            temp=self.top
            while temp is not None:
                print(temp.data,end="-->")
                temp=temp.next
            print("none")
        # else:
        #     raise IndexError("stack is empty")
s1=stack()
s1.push(10)
s1.push(20)
s1.push(30)
s1.push(40)
s1.display()
print(s1.peek())
print(s1.size())
s1.pop()
s1.display()
print()

"""
from SLL import *
class stack:
    def __init__(self):
        self.mylist= SLL()
        self.item_count=0
        
    def is_empty(self):
        return self.mylist.is_empty()
    
    def push(self,data):
        self.mylist.insert_at_start(data)
        self.item_count+=1
        
    def pop(self):
        if not self.is_empty():
            return self.mylist.delete_at_start()
        self.item_count-=1
        
    def peek(self):
        if not self.is_empty():
            return self.mylist.start.item
        else:
            raise IndexError("stack underflow")
        
    def size(self):
        return self.item_count
    
    def display(self):
        if not self.is_empty():
            temp=self.mylist
            while temp is not None:
                print(temp.item,end="-->")
                temp=temp.next
            print("none")
    
s1=stack()
s1.push(10)
s1.push(20)
s1.push(30)
s1.push(40)
s1.display()
print(s1.peek())
print(s1.size())
print()
"""