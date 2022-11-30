class Node:
    def _init_(self,data):
        self.data=data
        self.left=None
        self.right=None
        self.height=1
def getHeight(root):
    if root==None:
        return 0
    return root.height
def getBalanceFactor(root):
    if root==None:
        return 0
    return getHeight(root.left)-getHeight(root.right)
def rightRotate(root):
    x=root.left
    t2=x.right
    x.right=root
    root.left=t2
    root.height=1+max(getHeight(root.left),getHeight(root.right))
    x.height=1+max(getHeight(x.left),getHeight(x.right))
    return x
def leftRotate(root):
    y=root.right
    t2=y.left
    y.right=root
    root.right=t2
    root.height=1+max(getHeight(root.left),getHeight(root.right))
    y.height=1+max(getHeight(y.left),getHeight(y.right))
    return y
def insert(root,data):
    if root==None:
        return Node(data)
    if data<root.data:
        root.left=insert(root.left,data)
    else:
        root.right=insert(root.right,data)
    root.height=1+max(getHeight(root.left),getHeight(root.right))
    bf=getBalanceFactor(root)
    if bf>1:  
        if data<root.left.data:
            return rightRotate(root)
        else:
            root.left=rightRotate(root.right)
            return leftRotate(root)
    if bf<-1: 
        if data>root.right.data:
            return rightRotate(root)
        else:
            root.right=leftRotate(root.right)
            return rightRotate(root)
    return root
def inorder(root):
     if root!=None:
        inorder(root.left)
        print(root.data)
        inorder(root.right)
root=None
a=[33, 13, 52, 9, 21, 61, 8, 11]
for i in a:
    root=insert(root,i)
inorder(root)
