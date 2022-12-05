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

def check_bal(root):
    if root is None:
        return
    check_bal(root.left)
    if -1<=balfac(root)<=1:
        return True
    check_bal(root.right)
    return False

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
            root.left=leftrotate(root)
            return rightrotate(root)
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
    root=avl_ins(root,i)
levelorder(root)
# print(maxi(root))
# print(mini(root))
# print(check_bal(root))
