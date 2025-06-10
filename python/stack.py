class stack:
    def __init__(self,size):
        self.size=size
        self.stack=[0]*size
        self.top=-1
    def push(self,data):
        if self.top==self.size-1:
            print("overflow")
            return
        self.top+=1
        self.stack[self.top]=data   
    def pop(self):
        if self.top==-1:
            print("underflow")
            return
        self.top-=1
    def peek(self):
        if self.top==-1:
            print("underflow")
            return
        print(self.stack[self.top])
    def display(self):
        if self.top==-1:
            print("underflow")
            return
        for i in range(self.top,-1,-1):
            print(self.stack[i],end =" ")
        print()
obj=stack(3)
obj.push(5)
obj.push(3)
obj.push(7)
obj.display()
obj.pop()
obj.display()
obj.push(23)
obj.display()
obj.peek()
