"""queue=[]
def enqueue():
    n=int(input("enter the start element"))
    queue.append(n)
    print(queue)
    
def dequeue():
    n=int(input("enter the last element"))
    queue.pop()
    print(queue)
    
def display():
    if len(queue)==0:
        print("queue is empty")
    else:
        for elements in queue:
            print(elements, end="-->")
        print("the first element of queue", queue[0])
        
while (True):
    print("enter your option: " ,"1.enqueue, 2.dequeue, 3.display, 4.exit")
    option=int(input("option: " ,))
    if option==1:
        enqueue()
    if option==2:
        dequeue()
    if option==3:
        display()
    if option==4:
        exit()
        break
    # else:
    #     print("not available")
    # break"""
    
    
class queue:
    def __init__(self,data):
        self.data=data
        self.next=None

class queue_LL:
    def __init__(self):
        self.head=None
        self.tail=None

    def display(self):
        if self.head is None:
            print("queue is empty")
        else:
            temp=self.head
            while temp is not None:
                print(temp.data,end="-->")
                temp=temp.next
            print("none")

    def enqueue(self,data):
        n=queue(data)
        if self.head is None:
            self.head=n
            self.tail=n
        else:
            self.tail.next=n
            self.tail=n

    def dequeue(self):
        if self.head is None:
            print("queue is empty")
        else:
            self.head=self.head.next

q=queue_LL()
q.display()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()
q.dequeue()
q.display()

    