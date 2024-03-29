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

def rangesumBST(root,low,high):
    q=[]
    sum=0
    q.append(root)
    while len(q)!=0:
        top=q.pop(0)
        if low<=top.data<=high:
            sum+=top.data
        if top.left!=None:
            q.append(top.left)
        if top.right!=None:
            q.append(top.right)
    return sum

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

def del_leaf_all(l):
    for i in l:
        if leafall(root,i)==True:
            delete(root,i)
            
            
def findsucc(root,succ,key):
    if root is None:
        return succ
    if root.data == key:
        if root.right:
            return min(root.right)
    elif key < root.data:
        succ = root
        return findsucc(root.left, succ, key)
    else:
        return findsucc(root.right, succ, key)
    return succ

def height(root):
    if root is None:
        return 0
    return max(height(root.right),height(root.left))+1


def hneed(root,data,h):
    temp=height(root)
    if temp==h and root.data==data:
        print(root.data)
    if root.data<data:
        return hneed(root.right,data,h)
    if root.data>data:
        return hneed(root.left,data,h)
    
    
t1=[]
def parent(root,data,tem1=None):
    if data == root.data:
        t1.append(tem1)
        if len(t1)==2 and t1[0]==t1[1]:
            print(tem1)
        elif len(t1)==2:
            print("No node")
    if data<root.data:
        tem1=root.data
        parent(root.left,data,tem1)
    elif data>root.data:
        tem1=root.data
        parent(root.right,data,tem1)
        
            
def parent_del(root, data, tem1=None):
    if data == root.data:
        return delete(root, tem1)
    if data < root.data:
        tem1 = root.data
        parent(root.left, data, tem1)
    elif data > root.data:
        tem1 = root.data
        parent(root.right, data, tem1)


def child_del(root, data):
    if data == root.data:
        if root.left:
            delete(root, root.left.data)
        if root.right:
            delete(root, root.right.data)
        else:
            print("No childs")
    if data < root.data:
        child_del(root.left, data)
    elif data > root.data:
        child_del(root.right, data)
        
        
def insert(l,temp):
    global root
    if temp==True:
        for i in l:
            root=ins(root,i)
    else:
        root=non_ins(root,l[0])
        for i in range(1,len(l)):
            non_ins(root,l[i])
            
            
# l=[int(i) for i in input().split()]
l=[100,60,50,70,30,55,65,75,120,125]
root=None
insert(l,False)

#-- rangesumBST low and high
low=30
high=60
print(rangesumBST(root,low,high))

#-- height input

h=int(input(" Enter the required height:"))
for i in l:
    hneed(root,i,h)
print(height(root))

#-- find succ input

key=int(input("Enter the value:"))
succ=None
succ=findsucc(root,None,key)
print(succ.data)
del(root,succ.data)

#--finding parent and two child case input

l1=[int(i) for i in input("Enter Two childs:").split()]
for i in l1:
    parent(root,i,tem1=None)


