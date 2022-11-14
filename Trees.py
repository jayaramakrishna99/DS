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


root = None
l=[int(i) for i in input().split()]
for i in l:
    root=ins(root,i)

inorder(root)
