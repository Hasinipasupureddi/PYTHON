class Node:
    def __init__(self,data):                         #creating node
        self.data=data                               # to store value
        self.left=self.right=None                    #initially none
def inorder_traversal(root):                         #left root right
    if root:
        inorder_traversal(root.left)
        print(root.data,end=" ")
        inorder_traversal(root.right)
def preorder_traversal(root):                        #root left right
    if root:
        print(root.data,end=" ")
        preorder_traversal(root.left)
        preorder_traversal(root.right)
def postorder_traversal(root):                     #left right root
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.data,end=" ")
        
root=Node(5)                                       #to create a rootnode in tree
root.left=Node(3)
root.right=Node(7)
root.right.right=Node(9)
root.left.left=Node(6)
root.left.right=Node(10)
root.left.right.left=Node(13)                     #now we need to display- inorder traversal-left root right
inorder_traversal(root)
print()
preorder_traversal(root)
print()
postorder_traversal(root)
