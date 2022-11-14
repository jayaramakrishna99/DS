class Node:
    def __init__(self,data):
        self.left = None
        self.data = data
        self.right = None


def ins(root, data):
    if root is None:
        return Node(data)
    if root.data < data:
        root.right = ins(root.right, data)
    else:
        root.left = ins(root.left, data)
    return root

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


def search(root,data):
    if root == None:
        return False
    if root.data==data:
        return True
    if root.data<data:
        return search(root.right,data)
    if root.data>data:
        return search(root.left,data)

def levelorder(root):
    q=[]
    q.append(root)
    while len(q)!=0:
        top=q.pop(0)
        print(top.data)
        if top.left!=None:
            levelorder(root.left)
        if top.right!=None:
            levelorder(root.right)
            
# def non_ins(root,data):
#     newNode=Node(data)
#     x=root
#     y=None
#     while x!=None:
#         y=x
#         if data<x.data:
#             x=x.left
#         else:
#             x=x.right
#     if y==None:
#         y = newNode
#     elif data < y.data:
#         y.left = newNode
#     else:
#         y.right = newNode
#     return y


# def min(root):
#     min=root.right
#     while root.right!=None:
#         min =root.left
#     return min



# def deleteNode(root,data):
#     if root is None:
#         return root
#     if root.data<data:
#         root.right=deleteNode(root.right,data)
#     if root.data>data:
#         root.left=deleteNode(root.left,data)
#     else:
#         if root.left is None:
#             temp=root.right
#             root=None
#             return temp
#         if root.right is None:
#             temp=root.left
#             root=None
#             return temp
#         if root.left is None and root.right is None:
#             root=None
#         if root.left!=None and root.right!=None:
#             mini=min(root)
#             root=None
#             return mini   


root = None
l=[int(i) for i in input().split()]
for i in l:
    root=ins(root,i)

inorder(root)
