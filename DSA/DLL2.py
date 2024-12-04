class node:
    def __init__(self, prev=None, item=None, next=None):
        self.prev=prev
        self.item=item
        self.next=next
        
class DLL:
    def __init__(self, start=None):
        self.start=start
        
    def is_empty(self):
        return self.start==None
    
    def add_at_start(self,data):
        n=node(None,data,self.start)
        if not self.is_empty():
            self.start.prev=n
        self.start=n
        
        
    def add_at_end(self,data):
        temp=self.start
        # n=node(temp,data,None)
        while temp.next is not None:
            temp=temp.next
            
        n=node(temp,data,None)
        # if temp==None:
        #     temp=n
        # else:
        temp.next=n
        
    def search(self,data):
        temp=self.start
        while temp is not None:
            if temp.item==data:
                return temp
            temp=temp.next
        return None
        
    def add_after(self,temp,data):
        if temp is not None:
            n=node(temp,data,temp.next)
            if temp.next is not None:
                temp.next.prev=n
            temp.next=n
        
    def print_all(self):
        temp=self.start
        while temp is not None:
            print(temp.item,end="<-->")
            temp=temp.next
        print("none")
mylist=DLL()
mylist.add_at_start(22)
mylist.add_at_start(23)
mylist.add_at_start(24)
mylist.print_all()
mylist.add_at_end(27)
mylist.print_all()
mylist.add_after(mylist.search(23),8)
mylist.print_all()
print()

"""queue=[]
def enqueue():
    n=int(input("enter head/front element: "))
    queue.append(n)
    print(queue)
    
def dequeue():
    n=int(input("enter tail/rear element: "))
    queue.remove(n)
    # queue.pop(0)
    print(queue)
    
def display():
    if len(queue)==0:
        print("queue is empty")
    else:
        print("front element: ",queue[0],"\n","rear element: ",queue[-1])
            
while(True):
    print("enter your option:","1.enqueue, 2.deueue, 3.display, 4.exit")
    option=int(input("option: "))
    if option==1:
        enqueue()
    if option==2:
        dequeue()
    if option==3:
        display()
    if option==4:
        exit()
        break"""
    
"""class queue:
    def __init__(self,data):
        self.data=data
        self.next=None
    
class queue_LL:
    def __init__(self):
        self.start=None
        self.tail=None
        
    def enqueue(self,data):
        n=queue(data)
        if self.start is None:
            self.start=n
            self.tail=n
        else:
            self.tail.next=n
            self.tail=n
            
    def dequeue(self):
        if self.start is None:
            print("empty")
        else:
            self.start=self.start.next
        
    def display(self):
        if self.start is None:
            print("empty")
        else:
            temp=self.start
            while temp is not None:
                print(temp.data,end="-->")
                temp=temp.next
            print("none")
            
mylist=queue_LL()
mylist.enqueue(1)
mylist.enqueue(2)
mylist.enqueue(3)
mylist.enqueue(4)
mylist.enqueue(5)
mylist.display()
mylist.dequeue()
mylist.display()"""

class stack:
    def __init__(self):
        self.n=[]
        
    def is_empty(self):
        return len(self.n)==0
    
    def push(self,data):
        # if not self.is_empty():
        self.n.append(data)
        # else:
        #     raise IndexError("stackoverflow")
        
    def pop(self):
        if not self.is_empty():
            return self.n.pop()
        else:
            raise IndexError("stackunderflow")
        
    def peek(self):
        if not self.is_empty():
            return self.n[-1]
        else:
            raise IndexError("empty")
        
    def size(self):
        return len(self.n)
    
    def display(self):
        if not self.is_empty():
            print(self.n)
        else:
            return IndexError("empty")
        
p=stack()
p.push(11)
p.push(12)
p.push(13)
p.push(14)
p.display()
print(p.peek())
p.pop()
p.display()
print(p.size())
# print()