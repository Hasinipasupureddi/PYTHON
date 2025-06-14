class Queue:
    def __init__(self,size):
        self.queue=[]
    def enqueue(self,data):
        self.queue.append(data)
    def dequeue(self):
        if len(self.queue):
           self.queue.pop(0)
        else:
            print("is empty")
    def peek(self):
        if len(self.queue):
            print(self.queue[0])
        else:
            print("is empty")
    def display(self):
        if len(self.queue):
            for i in self.queue:
               print(i,end=" ")
            print()
        else:
            print("is empty")
obj=Queue(3)
obj.enqueue(17)
obj.enqueue(12)
obj.enqueue(7)
obj.display()
obj.dequeue()
obj.display()
obj.enqueue(23)
obj.display()
obj.peek()
