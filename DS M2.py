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

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data)
    inorder(root.right)

def maxi(root):
    while root.right!=None:
        root=root.right
    return root.data

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

def leftrotate(root):
    

def avl_ins(root,data):
    if root is None:
        return
    if root.data<data:
        root.right = avl_ins(root.right,data)
    elif root.data>data:
        root.left = avl_ins(root.left,data)
    h=height(root)
    b=balfac(root)
    if b>1:
        if root.left.data>data:
            return rightrotate(root)
        else:
            root.left=leftrotate(root)
            return rightright(root)
    if b<-1:
        if root.right.data<data:
            return leftrotate(root)
        else:
            root.left=rightrotate(root)
            return leftrotate(root)
    return root


root=None
# l=[int(i) for i in input("Enter the list:").split()]
l=[100,60,50,70,30,55,65,75,120,125]
for i in l:
    root=bst_ins(root,i)

print(maxi(root))
print(mini(root))
