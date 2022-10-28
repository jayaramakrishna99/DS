class stack:
    def __init__(self):
        self.l = []

    def push(self, data):
        self.l.append(data)

    def pop(self):
        return self.l.pop()

    def empty(self):
        return self.l == []

    def prints(self):
        for i in reversed(self.l):
            print(i)


def bottom_insert(self, data):
    if self.empty():
        self.push(data)
    else:
        popped = self.pop()
        bottom_insert(self, data)
        self.push(popped)


def reverse(s):
    if s.empty():
        pass
    else:
        popped = s.pop()
        reverse(s)
        bottom_insert(s, popped)


s = stack()
s.push(1)
s.push(2)
s.push(3)
s.push(5)
s.push(6)
s.prints()
print()
reverse(s)
s.prints()
