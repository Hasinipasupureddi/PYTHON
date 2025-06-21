class Node:
    def __init__(self,data):
        self.data=data
        self.left=self.right=None
class BST:
    def __init__(self):
        self.root=None
    def insert(self,data):
        self.root=self.rec_insert(self.root,data)
    def rec_insert(self,root,data):
        if root is None:
            return Node(data)
        elif data<root.data:
            root.left=self.rec_insert(root.left,data)
        else:
            root.right=self.rec_insert(root.right,data)
        return root
    def inorder(self,root):                     
        if root:
            self.inorder(root.left)
            print(root.data,end=" ")
            self.inorder(root.right)               
    def preorder(self,root):                     
        if root:
            print(root.data,end=" ")
            self.preorder(root.left)
            self.preorder(root.right)
    def postorder(self,root):                     
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data,end=" ")


obj=BST()
obj.insert(7)    #alternate method-
obj.insert(6)  #insert_data=list(map(int,input().split())) or list=[7,6,1,4,10,12]
obj.insert(1)       #for i in insert data
obj.insert(4)       #obj.insert(i)
obj.insert(10)
obj.insert(12)
obj.inorder(obj.root)
print()
obj.preorder(obj.root)
print()
obj.postorder(obj.root)
#output=
1 4 6 7 10 12 
7 6 1 4 10 12 
4 1 6 12 10 7
