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
        
        def insert_at_start(self,data):
            n=node(None,data,self.start)
            if not self.is_empty():
                self.start.prev=n
            self.start=n
            
        def insert_at_last(self,data):
            temp=self.start
            if self.start is not None:
                while temp.next is not None:
                    temp=temp.next
                    
                n=node(temp,data,None)
                if temp==None:
                    self.start=n
                else:
                    temp.next=n
            
        def search(self,data):
            temp=self.start
            while temp is not None:
                if temp.item==data:
                    return temp
                temp=temp.next
            return None
        
        def insert_after(self,temp,data):
            if temp is not None:
                n=node(temp,data,temp.next)
                if temp.next is not None:
                    temp.next.prev=n
                temp.next=n
        
        def print_all_elements(self):
            temp=self.start
            while temp is not None:
                print(temp.item,end="<-->")
                temp=temp.next
            print("None")
            
        def delete_first(self):
            if self.start is not None:
                self.start=self.start.next
                # if self.start is not None:
                #     self.start.prev=None
                    
        def delete_last(self):
            if self.start is None:
                pass
            elif self.start.next is None:
                self.start=None
            else:
                temp=self.start
                while temp.next is not None:
                    temp=temp.next
                temp.prev.next=None
                
        def delete_after(self,data):
            if self.start is None:
                pass
            else:
                temp=self.start
                while temp is not None:
                    if temp.item==data:
                        if temp.next is not None:
                            temp.next.prev=temp.prev
                        if temp.prev is not None:
                            temp.prev.next=temp.next
                        else:
                            self.start=temp.next
                            break
                    temp=temp.next
            
mylist=DLL()
mylist.insert_at_start(10)
mylist.insert_at_start(20)
mylist.insert_at_start(30)
mylist.print_all_elements()
mylist.insert_at_last(40)
mylist.print_all_elements()
mylist.insert_after(mylist.search(20),25)
mylist.print_all_elements()
print()

mylist.delete_first()
mylist.print_all_elements()
mylist.delete_last()
mylist.print_all_elements()
mylist.delete_after(20)
mylist.print_all_elements()
print()