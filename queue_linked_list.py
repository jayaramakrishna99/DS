class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:

    def __int__(self):
        self.head = None
        self.last = None

    def enqueue(self, data):
        if self.last is None:
            self.head = Node(data)
            self.head = self.head.next
        else:
            self.head.next=Node(data)
            self.
