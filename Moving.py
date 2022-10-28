class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class SLL:
    def __init__(self):
        self.head = None
        self.last_node = None

    def print(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next

    def append(self, data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next

    def movelf(self):
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next.next = self.head
        self.head = temp.next
        temp.next = None

    def movefl(self):
        temp = self.head
        while temp:
            self.head = temp.next.next
            temp.next = temp
            temp.next = None


l = SLL()
n = int(input('n no--->'))
for i in range(n):
    data = int(input('data-->'))
    l.append(data)
l.movefl()
l.print()
