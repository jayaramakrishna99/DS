class Node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None
# Inserting values in BST Tree
def bst_ins(root,data):
    if root is None:
        return Node(data)
    if root.data<data:
        root.right=bst_ins(root.right,data)
    else:
        root.left=bst_ins(root.left,data)
    return root

# Level order Traversal
def levelorder(root):
    q=[]
    q.append(root)
    while len(q)!=0:
        top=q.pop(0)
        print(top.data)
        if top.left!=None:
            q.append(top.left)
        if top.right!=None:
            q.append(top.right)

# A. Maximum Element in the BST
def maxi(root):
    while root.right!=None:
        root=root.right
    return root.data

# Height of the Tree
def height(root):
    if root is None:
        return 0
    return max(height(root.left),height(root.right))+1
# Balance factor of root
def balfac(root):
    return height(root.left)-height(root.right)

# B. Checking Balancing factor of root in BST
def check_bal(root):
    if root is None:
        return
    check_bal(root.left)
    if -1<=balfac(root)<=1:
        return True
    check_bal(root.right)
    return False
# Right rotation
def rightrotate(root):
    temp=root.left
    t=temp.right
    temp.right=root
    root.left=t
    return temp
# Left rotation
def leftrotate(root):
    temp=root.right
    t=temp.left
    temp.left=root
    root.right=t
    return temp
# Inserting values in AVl Tree
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
# l=[100,70,50,40,60,75,80]
root=None
l=[int(i) for i in input().split()]
for i in l:
    root=bst_ins(root,i)
print("maximum element:",maxi(root))
levelorder(root)
if check_bal(root)==True:
    print("BST is balanced and It is AVL.")
else:
    print("BST is Not Balanced and Balanced is")
    root1=None
    for i in l:
        root1=avl_ins(root1,i)
    levelorder(root1)

