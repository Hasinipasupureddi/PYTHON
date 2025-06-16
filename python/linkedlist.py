
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def insert(self,data):            
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
            return
        cur=self.head
        while cur.next:
            cur=cur.next
        cur.next=newnode
    
    def display(self):
        if self.head is None:
            print("no data found")
            return
        cur=self.head
        while cur:
            print(cur.data,end="->")
            cur=cur.next
    
    def b_insert1(self,data):                    #insert new node at the beggining
        newnode=Node(data)
        newnode.next=self.head
        self.head=newnode
    def b_delete(self):                          #to delete node at the beginning
        if self.head is not None:                # works without the if satement also
            self.head=self.head.next             
    
    def e_delete(self):                                  #delete node at the end
        if not self.head or self.head.next is None:     #works without if statement also
            self.head=None
            return
        cur=self.head
        while cur.next.next:                     #checking last but one value
            cur=cur.next
        cur.next=None
        
    def position(self,pos):                      #to find position of the node
        if pos<=0:
            return "invalid position"
        cur=self.head
        for i in range(pos-1):
            if cur.next is None: 
                break
            cur=cur.next
        else: return cur              
        return -1
    
    def insert_by_position(self,data,pos):          #insert at any position
        newnode=Node(data)
        if pos == 1:
            self.b_insert1(data)
            return
        cur=self.position(pos-1)       
        if cur==-1:
            print("no pos")
            return 
        newnode.next=cur.next
        cur.next= newnode

    def delete_by_position(self,pos):               #delete at any position  
        if pos==1:
            self.b_insert1()
            return
        cur=self.position(pos-1)
        if cur==-1:
            print("no pos")
            return
        cur.next=cur.next.next
        '''
#alternate for del by position
    def delete_by_position(self,pos):
        if self.head is None:
            print("list is empty")
            return
        if pos<1:
            print("invalid position")
            return
        if pos == 1:
            self.head=self.head.next
            return
        cur=self.head
        for i in range(pos-2):
            if cur is None or cur.next is None:
                print("no such position")
                return
            cur=cur.next
        if cur.next is None:
            print("no such position")
            return
    '''
    def reverse(self):                           #reverse the linked list
        prev=None
        cur=self.head
        while cur is not None:
            nextnode=cur.next
            cur.next=prev
            prev=cur
            cur=nextnode
        self.head=prev
obj=linkedlist()
obj.insert(5)
obj.insert(10)
obj.insert(15)
obj.insert(30)
obj.b_insert1(25)
obj.display()
obj.b_delete()
print()
obj.display()
obj.e_delete()
print()
obj.display()
print()
print(obj.position(3).data)
obj.insert_by_position(70,1)
obj.display()
print()
obj.delete_by_position(3)
obj.display()
print()
print("original:")
obj.display()
print()
print("reversed:")
obj.reverse()
obj.display()

'''#output=
25->5->10->15->30->
5->10->15->30->
5->10->15->
15
70->5->10->15->
70->5->15->
original:
70->5->15->
reversed:
15->5->70->'''
