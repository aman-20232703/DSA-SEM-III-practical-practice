class queue:
    def __init__(self):
        self.elements=[]
        # self.front=None
        # self.rare=None
        
    def is_empty(self):
        return len(self.elements)==0
    
    def enqueue(self,data):
        self.elements.append(data)
        
    def dequeue(self):
        if not self.is_empty():
            self.elements.pop(0)
        else:
            raise IndexError("queue underflow")
        
    def get_front(self):
        if not self.is_empty():
            return self.elements[0]
        else:
            raise IndexError("queue underflow")
        
    def get_rear(self):
        if not self.is_empty():
            return self.elements[-1]
        else:
            raise IndexError("queue underflow")
        
    def size(self):
        return len(self.elements)
    
q1=queue()
try:
    print(q1.get_front())
except IndexError as e:
    print(e.args[0])
    
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
q1.enqueue(40)
q1.enqueue(50)
print("front value:-", q1.get_front(),"and rear value:-",q1.get_rear())

try:
    q1.dequeue()
    print("queue has now ",q1.size(),"elements")
except IndexError as e:
    print(e.args[0])
    
    
"""class queue:
    def __init__(self):
        self.elements=[]
        # self.front=None
        # self.rare=None
        
    def is_empty(self):
        return len(self.elements)==0
    
    def enqueue(self,data):
        self.elements.append(data)
        
    def dequeue(self):
        if not self.is_empty():
            self.elements.pop(0)
        else:
            raise IndexError("queue underflow")
        
    def get_front(self):
        if not self.is_empty():
            return self.elements[0]
        else:
            raise IndexError("queue underflow")
        
    def get_rear(self):
        if not self.is_empty():
            return self.elements[-1]
        else:
            raise IndexError("queue underflow")
        
    def size(self):
        return len(self.elements)
    
    # def queue(self):
    #     print(enqueue[0:])
    
q1=queue()
try:
    print(q1.get_front())
except IndexError as e:
    print(e.args[0])

q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
q1.enqueue(40)
q1.enqueue(50)
print("front value:-", q1.get_front(),"and rear value:-",q1.get_rear())

# q1.queue()
# print()

try:
    q1.dequeue()
    print("queue has now ",q1.size(),"elements")
except IndexError as e:
    print(e.args[0])"""
    