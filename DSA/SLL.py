"""# Define a class node to describe a node of a singly linked list
class node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
 
# Define a class SLL to implememt Singly Linked List with init() method to create and initialise start reference variable
class SLL:
    def __init__(self,start=None):
        self.start=start
        
# Define a method is empty() to check if the linked list is empty in SLL class
    def is_empty(self):
        return self.start==None
    
# In class SLL, define a method insert_at_start() to insert an element at the starting of the list
    def insert_at_start(self,data):
        n=node(data,self.start)
        self.start=n
     
# In class SLL, define a method insert_at_end() to insert an element at the end of the list   
    def insert_at_end(self,data):
        n=node(data)
        if not self.is_empty():
            temp=self.start #self.start=start
            while temp.next is not None:
                temp=temp.next
            temp.next=n
        else:
            self.start=n
            
# In class SLL, define a method search() to find the node with specified element value
    def search(self,data):
        temp=self.start
        while temp is not None:
            if temp.item==data:
                return temp
            temp=temp.next
        return None
    
# In class, define a method insert_after() to insert a new node after a given node of the list 
    def insert_after(self,temp,data):
        if temp is not None:
            n=node(data,temp.next)
            temp.next=n
            
# Define a function to print all the elements of the list
    def print_all_list(self):
        temp=self.start
        while temp is not None:
            print(temp.item,end="-->")
            temp=temp.next
            
        print("none")
        
        
mylist=SLL()
mylist.insert_at_start(10)
mylist.insert_at_start(20)
mylist.insert_at_end(30)
mylist.insert_after(mylist.search(20),25)
mylist.print_all_list()"""



# Define a class node to describe a node of a singly linked list
class node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
        
# Define a class SLL to implememt Singly Linked List with init() method to create and initialise start reference variable
class SLL:
    def __init__(self,start=None):
        self.start=start
        
# In SLL class, Define a method is_empty() to check if the linked list is empty
    def is_empty(self):
        return self.start==None
    
# In class SLL, define a method insert_at_start() to insert an element at the starting of the list
    def insert_at_start(self,data):
        n=node(data,self.start)
        self.start=n
    
# In class SLL, define a method insert_at_end() to insert an element at the end of the list
    def insert_at_end(self,data):
        n=node(data)
        if not self.is_empty():
            temp=self.start #self.start=start
            while temp.next is not None:
                temp=temp.next
            temp.next=n
        else:
            self.start=n
            
# In class SLL, define a method search() to find the node with specified element value
    def search(self,data):
        temp=self.start
        while temp is not None:
            if temp.item==data:
                return temp
            temp=temp.next
        return None
    
# In class, define a method insert_after() to insert a new node after a given node of the list
    def insert_after(self,temp,data):
        if temp is not None:
            n=node(data,temp.next)
            temp.next=n

# Define a function to print all the elements of the list
    def print_all_list(self):
        temp=self.start
        while temp is not None:
            print(temp.item,end="-->")
            temp=temp.next

        print("none")
    
    
#In class SLL, define a method delete_first() to delete first element from the list.
    def delete_at_start(self):
        if self.start is not None:
            self.start=self.start.next

#In class SLL, define a method delete_last() to delete last element from the list.
    def delete_at_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start=None
        else:
            temp=self.start
            while temp.next.next is not None:
                temp=temp.next
            temp.next=None
            #In class SLL, define a method delete_item() to delete specified element from the list.
    def delete_after(self,data):
        if self.start is None:
            pass
        elif self.start.next is None:
            if self.start.item==data:
                self.start=None
        else:
            temp=self.start
            if temp.item==data:
                self.start=temp.next
            else:
                while temp is not None:
                    if temp.next.item==data:
                        temp.next=temp.next.next
                        break
                    temp=temp.next
        
mylist=SLL()

mylist.insert_at_start(10)
mylist.insert_at_start(20)
mylist.insert_at_start(30)
mylist.insert_at_start(40)
mylist.print_all_list()
mylist.insert_at_end(40)
mylist.print_all_list()
mylist.insert_after(mylist.search(20),25)
mylist.print_all_list()
print()

mylist.delete_at_start()
mylist.print_all_list()
mylist.delete_at_last()
mylist.print_all_list()
mylist.delete_after(25)
mylist.print_all_list()
print()


"""class node:
    def __init__(self, item=None, next=None):
        self.item=item
        self.next=next
        
class SLL:
    def __init__(self,start=None):
        self.start=start
        
    def is_empty(self):
        return self.start==None
    
    def insert_start(self,data):
        n=node(data,self.start)
        self.start=n
        
    def insert_end(self,data):
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
            
    def print_all(self):
        temp=self.start
        while temp is not None:
            print(temp.item,end="-->")
            temp=temp.next
        print("none")
        
    def delete_start(self):
        # temp=self.start
        if self.start is not None:
            self.start=self.start.next
            
    def delete_end(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start=None
        else:
            temp=self.start
            while temp.next.next is not None:
                temp=temp.next
            temp.next=None
            
    def delete_at_any(self,data):
        if self.start is None:
            pass
        elif self.start.next is None:
            if self.start.item==data:
                self.start=None
        else:
            temp=self.start
            if temp.item==data:
                self.start=None
            else:
                while temp.next is not None:
                    if temp.next.item==data:
                        temp.next=temp.next.next
                        break
                    temp=temp.next
            
        
mylist= SLL()
mylist.insert_start(10)
mylist.insert_start(20)
mylist.insert_start(30)
mylist.insert_start(40)
mylist.print_all()
mylist.insert_after(mylist.search(20),25)
mylist.print_all()
mylist.insert_end(50)
mylist.print_all()
print()


mylist.delete_start()
mylist.print_all()
mylist.delete_at_any(20)
mylist.print_all()
mylist.delete_end()
mylist.print_all()
print()"""










"""class Node:
    def _init_(self, data):
        self.data = data
        self.ref = None


class LinkedList:
    def _init_(self):
        self.head = None

    # The display function is now an attribute of the LinkedList class.
    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, "-->", end=" ")
                n = n.ref

    def add_begin( self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node
    def add_end( self,data):
        if self.head is None:
            print("Linked list is empty")
        else:
            new_node = Node(data)
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node
    def add_after( self,data,x):
        if self.head is None:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
        else:
            n = self.head
            while n is not None:
                if n.data == x:
                    break
                n = n.ref
            if n is None:
                print("Node is not present in LL")
            else:
                new_node = Node(data)
                new_node.ref = n.ref
                n.ref = new_node

    def del_start( self):
        if self.head is None:
            print("Linked list is empty")
        else:
            self.head = self.head.ref
    def del_end( self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None

    def del_after(self,x):
        if self.head is None:
            print("Linked list is empty")
        else:
            n = self.head
            while n is not None:
                if n.data == x:
                    break
                n = n.ref
            if n is None:
                print("Node is not present in LL")
            else:
                n.ref = n.ref.ref


link1 = LinkedList()
link1.display()
print("\n add at beginning")
link1.add_begin(10)
link1.add_begin(20)
link1.add_begin(30)
link1.display()
print("\n add at end")
link1.add_end(40)
link1.display()
print("\n add after")
link1.add_after(50,30)
link1.display
print("\n del start")
link1.del_start()
link1.display()
print("\n del end")
link1.del_end()
link1.display()
print("\n del value")
link1.del_after(20)
link1.display()"""