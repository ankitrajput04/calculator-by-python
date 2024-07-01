# print("1 for add")
# print("2 for sub")
# print("3 for mul")
# print("4 for div")
# a = int(input("Enter your choice for calculate"))
# x = int(input("Enter first value:"))
# y = int(input("Enter second value:"))

# if(a==1):
#     z = x+y
#     print(z)
# elif(a==2):
#     z = x-y
#     print(z)
# elif(a==3):
#     z = x*y
#     print(z)
# elif(a==4):
#     z = x/y
#     print(z)
# else:
#     print("nothing")

class one:
    def __init__(self,x,y):
        self.first = x
        self.second = y
        # self.second1 = a
    
    def add(self):
        z = self.first+self.second
        print(z)

    def sub(self):
        z = self.first-self.second
        print(z)
    
    def mul(self):
        z = self.first*self.second
        print(z)
    def div(self):
        z = self.first/self.second
        print(z)
a = input("Enter operator:")
x = int(input("Enter first value:"))
y = int(input("Enter second value:"))

v = one(x,y)

while(True):
    if(a=="+"):
        v.add()
        break
       
    elif(a=="-"):
        v.sub()
        break
    elif(a=="*"):
        v.mul()
        break
    elif(a=="/"):
        v.div()
        break
    else:
        break


