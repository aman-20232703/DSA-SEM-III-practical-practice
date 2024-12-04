# i=0
# while i<5:
#     print(i==3)
#     break
# i+=1


# for i in range(2,21,2):
#     print(i)


# for i in range(5):
#     pass

# print("wow")


# x = [1,2,3,4,5,6]
# for n in x:
#     print(n)
# else:
#     print("end")


# s = "aman"
# for i in s:
#     if(i=='n'):
#         print("found")
#         break
#     print(i)
# else:
#     print("end")


# x = [1,4,9,16,25,36,49,64,81]

# for i in x:
#     print(i)
# i=0
# while i < len(x):
#     print(x[i])
#     i+=1


# for i in range(100,1,-1):
#     print(i)


# n = 5 #int(input("number: "))
# sum = 0

# for i in range(1,n+1):
#     sum+=i
# print("sum is: ",sum)


# n = 5 #int(input("number: "))
# sum = 0
# i=0

# while i<=n:
#     sum+=i
#     i+=1
# print("sum is: ",sum)


# n=5
# fact=1
# i=1

# while i <= n:
#     fact*=i
#     i+=1
# print(fact)


# n=5
# fact=1
#i=1

# for i in range(1,n+1):
#     fact*=i
#     #i+=1
# print(fact)


# import array as arr
# a=arr.array('i',[1,2,3,4,5,6,7,8,9,10])
# i=0
# while i<len(a):
#     if(i==3):
#         i+=1
#     print(a[i])

"""class test: #class or class object
    def __init__(self,a,b): #local variable
        # self.a=5 #instance object variable
        # self.b=6
        self.a=a
        self.b=b
        
# t1=test() #instance object
# t2=test()

t1=test(4,5)
t2=test(3,6)

print(t1.a,t1.b)
print(t2.a,t2.b)"""




"""class Test:
    x=5
    def __init__(self,a,b):
        self.a=a
        self.b=b
        
    def show(self):
        print(self.a,self.b)
    
    @staticmethod
    def f2():
        print("hello")
    
    @classmethod
    def f3(cls):
        print(cls.x)
    
    t1=test(3,4)
    t2=test(5,6)
    t1.show() # 1st argument implicitly pass in instance method
    t2.show()
    
    test.f3() # 1st argument implicitly pass in class method
    
    test.f2() # there is no any implicit argument which passes in static method"""




class employee:
    def __init__(self,empid,name,salary):
        self.empid=empid
        self.name=name
        self.salary=salary
        
    """def setempid(self,empid):
        self.empid=empid
    def setname(self,name):
        self.name=name
    def setsalary(self,salary):
        self.salary=salary
        
    def getempid(self):
        return self.empid
    def getname(self):
        return self.name
    def getsalary(self):
        return self.salary
    
e2=employee()
e2=employee(1,"aman",60000)
e1.setempid(1)
e1.setname("akash")
e1.setsalary(70000)
print(e1.getempid(),e1.getname(),e1.getsalary())
print(e2.getempid(),e2.getname(),e2.getsalary())"""

e1=employee(1,"sahil",60000)
e2=employee(2,"aman",600000)

print(e1.empid,e1.name,e1.salary)
print(e2.empid,e2.name,e2.salary)