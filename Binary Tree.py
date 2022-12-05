class Node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None
def BT():
    x=int(input("the data or 'N' for No Node:"))
    if x==-1:
        return None
    root=Node(x)
    print("Enter the left child of",x,'is')
    root.left=BT()
    print('Enter the right child of',x,'is')
    root.right=BT()
    return root

def inorder(root):
    if root==None:
        return None
    inorder(root.left)
    print(root.data)
    inorder(root.right)

def search(root,data):
    if root is None:
        return None
    search(root.left,data)
    if root.data==data:
        return True
    search(root.right,data)

root=BT()
inorder(root)
x=int(input('Enter the data:'))
search(root,x)