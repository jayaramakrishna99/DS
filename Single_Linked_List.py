class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


class ll:
    def __init__(self):
        self.head=None


    def print(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next


    def insert(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=new_node


    def insert_start(self,data):
        new_node=Node(data)
        temp=self.head
        self.head=new_node
        new_node.next=temp


    def insert_end(self,data):
        new_node=Node(data)
        temp=self.head
        while temp.next!=None:
            temp=temp.next
        temp.next=new_node


    def insert_pos(self,pos,data):
        new_node=Node(data)
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        new_node.next=temp.next
        temp.next=new_node


    def printll(self,f):
        temp = f
        while temp:
            print(temp.data, end=' ')
            temp = temp.next


    def odd_even(self):
        odd=Node(-1)
        even=Node(-1)
        temp1=odd
        temp2=even
        head=self.head
        while head:
            if head.data%2!=0:
                temp1.next=Node(head.data)
                temp1=temp1.next
            else:
                temp2.next=Node(head.data)
                temp2=temp2.next
            head=head.next
        temp1.next=even.next
        return odd.next
                    

    def find_mid(self):
        length=self.head
        c=0
        while length:
            c+=1
            length=length.next
        if c%2==0:
            half=c//2
        else:
            half=c//2+1
        temp=self.head
        for i in range(half-1):
            temp=temp.next
        mid=temp.data
        # temp1=self.head
        # temp2=self.head
        # while temp2.next.next!=None:
        #     temp1=temp1.next
        #     temp2=temp2.next.next
        # print(temp1.data)
        return mid
    

    def reverse(self):
        temp=self.head
        rev=None
        while temp:
            temp_rev=rev
            rev=Node(temp.data)
            rev.next=temp_rev
            temp=temp.next
        return rev
        

l=ll()
list=[5,2,3,3,0,1]
for i in list:
    l.insert(i)

# l.insert_start(7)
# l.insert_pos(3,7)
# l.insert_end(21)
    
#-------  ODD_EVEN  -------
# f=l.odd_even()
# l.printll(f)

#-------  Find Mid  -------
# l.find_mid()
# l.print()
    
#-------  Reverse LL  -------
# f=l.reverse()
# l.printll(f)