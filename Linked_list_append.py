class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SLL:
    def __init__(self):
        self.head = None

    def print(self):
        temp = self.head
        while temp:
            print(temp.data, end='')
            temp = temp.next

    def insert_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_end(self, data):
        new_node = Node(data)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def insert_pos(self, pos, data):
        new_node = Node(data)
        temp = self.head
        for i in range(pos - 1):
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node
    def delete_start(self):


l = SLL()
first = Node('j')
second = Node('r')
third = Node('k')
l.head = first
first.next = second
second.next = third
l.insert_start('ch ')
l.insert_end(3)
l.insert_end(7)
l.insert_pos(3, 9)
l.print()
