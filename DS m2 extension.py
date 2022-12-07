class Node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None

def bst_ins(root,data):
    if root is None:
        return Node(data)
    if root.data<data:
        root.right=bst_ins(root.right,data)
    else:
        root.left=bst_ins(root.left,data)
    return root

def mini(root):
    while root.left!=None:
        root=root.left
    return root.data

def height(root):
    if root is None:
        return 0
    return max(height(root.left),height(root.right))+1

def balfac(root):
    return height(root.left)-height(root.right)

def rightrotate(root):
    temp=root.left
    t=temp.right
    temp.right=root
    root.left=t
    return temp

def leftrotate(root):
    temp=root.right
    t=temp.left
    temp.left=root
    root.right=t
    return temp

def avl_ins(root,data):
    if root is None:
        return Node(data)
    if root.data<data:
        root.right = avl_ins(root.right,data)
    elif root.data>data:
        root.left = avl_ins(root.left,data)
    b=balfac(root)
    if b>1:
        if root.left.data>data:
            return rightrotate(root)
        else:
            root.left=leftrotate(root.left)
            return rightrotate(root)
    if b<-1:
        if root.right.data<data:
            return leftrotate(root)
        else:
            root.right=rightrotate(root.right)
            return leftrotate(root)
    return root

# Searching comparisons in BST and AVL
def search(root,data,c=0):
    c+=1
    if root is None:
        return
    if root.data==data:
        print("Found in",c)
    if root.data<data:
        search(root.right,data,c)
    elif root.data>data:
        search(root.left,data,c)

# Insertion and Searching in BST
root=None
# l=[100,70,50,40,60,75,80]
l=[int(i) for i in input("Enter the List:").split()]
n=int(input("Enter the data You want search:"))
for i in l:
    root=bst_ins(root,i)
print("the min value:",mini(root))
search(root,n)

# Insertion and Searching in AVL
root1=None
for i in l:
    root1=avl_ins(root1,i)
search(root1,n)

