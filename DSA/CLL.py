class node:
    def __init__(self,elements=None,next=None):
        self.elements=elements
        self.next=next
    
class CLL:
    def __init__(self,last=None):
        self.last=last
        
    def is_empty(self):
        return self.last == None
    
    def insert_at_start(self,data):
        n=node(data)
        if self.is_empty():
            n.next=n
            self.last=n
        else:
            n.next=self.last.next
            self.last.next=n
            
    def insert_at_last(self,data):
        n=node(data)
        if self.is_empty():
            n.next=n
            self.last=n
        else:
            n.next=self.last.next
            self.last.next=n
            self.last=n
            
    def search(self,data):
        if self.is_empty():
            return None
        temp=self.last.next
        while temp!=self.last:
            if temp.elements==data:
                return temp
            temp=temp.next
        if temp.elements==data:
            return temp
        return None
    
    def insert_after(self,temp,data):
        if temp is not None:
            n=node(data,temp.next)
            temp.next=n
            if temp==self.last:
                self.last=n
                
    def print_all(self):
        if not self.is_empty():
            temp=self.last.next
            while temp!=self.last:
                print(temp.elements,end="-->")
                temp=temp.next
            print(temp.elements)
                
    def delete_start(self):
        if not self.is_empty():
            self.last.next=self.last
            self.last=None
        else:
            self.last.next=self.last.next.next
            
    def delete_last(self):
        if not self.is_empty():
            if self.last.next==self.last:
                self.last=None
            else:
                temp=self.last.next
                while temp.next!=self.last:
                    temp=temp.next
                temp.next=self.last.next
                self.last=temp
            
    def delete_after(self,data):
        if not self.is_empty():
            if self.last.next==self.last:
                if self.last.elements==data:
                    self.last=None
            else:
                if self.last.next.elements==data:
                    self.delete_start()
                else:
                    temp=self.last.next
                    while temp!=self.last:
                        if temp.next==self.last:
                            self.delete_last()
                            break
                        if temp.elements==data:
                            temp.next=temp.next.next
                            break
                        temp=temp.next
                
    # def print_all(self):
    #     if not self.is_empty():
    #         temp=self.last.next
    #         while temp!=self.last:
    #             print(temp.elements,end="-->")
    #             temp=temp.next
    #         print(temp.elements)
        
        
mylist=CLL()
mylist.insert_at_start(40)
mylist.insert_at_start(30)
mylist.insert_at_start(20)
mylist.insert_at_start(10)
mylist.print_all()
mylist.insert_at_last(5)
mylist.print_all()
mylist.insert_after(mylist.search(30),35)
mylist.print_all()
print()

mylist.delete_start()
mylist.delete_last()
mylist.delete_after(20)
mylist.print_all()
print()