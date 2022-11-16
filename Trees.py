class Node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None
def ins(root,data):
    if root==None:
        return Node(data)
    if root.data<data:
        root.right=ins(root.right,data)
    else:
        root.left=ins(root.left,data)
    return root

def search(root,data):
    if root==None:
        return False
    if root.data==data:
        return True
    if root.data<data:
        return search(root.right,data)
    if root.data>data:
        return search(root.left,data)
    
def preorder(root):
    if root is None:
        return
    print(root.data)
    preorder(root.left)
    preorder(root.right)

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data)
    inorder(root.right)

def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data)

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

def non_ins(root,data):
    x=root
    y=None
    while x!=None:
        y=x
        if x.data<data:
            x=x.right
        else:
            x=x.left
    if y==None:
        y=Node(data)
    elif data<y.data:
        y.left=Node(data)
    else:
        y.right=Node(data)
    return y
        
def delete(root,data):
    if root is None:
        return root
    if root.data<data:
        root.right=delete(root.right,data)
    elif root.data>data:
        root.left=delete(root.left,data)
    else:
        if root.left==None and root.right==None:
            root=None
            return root

        if root.left is None:
            temp=root.right
            root=None
            return temp
        elif root.right is None:
            temp=root.left
            root=None
            return temp
        if root.left is not None and root.right is not None:
            temp=min(root.right)
            root.data=temp.data
            root.right=delete(root.right,temp.data)

    return root

def min(root):
    while root.left!=None:
        root=root.left
    return root

def leafall(root,data):
    # if (root.data==data or root.data!=data) and (root.left!=None or root.right!=None):
    #     return False
    if root.left is None and root.right is None:
        return True
    if root.data<data:
        return leafall(root.right,data)
    if root.data>data:
        return leafall(root.left,data)
    return False







# l=[int(i) for i in input().split()]
l=[100,60,50,70,30,55,65,75,120,125]
root=None
def insert(l,temp):
    global root
    if temp==True:
        for i in l:
            root=ins(root,i)
    else:
        root=non_ins(root,l[0])
        for i in range(1,len(l)):
            non_ins(root,l[i])


def del_leaf_all(l):
    for i in l:
        if leafall(root,i)==True:
            delete(root,i)
        
        

insert(l,False)
levelorder(root)
