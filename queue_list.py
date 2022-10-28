q = []


def enqueue(size):
    if len(q) == size:
        print('queue is full')
    else:
        n = int(input('enter the element'))
        q.append(n)
        print(n, 'is added')


def dequeue():
    if len(q) == 0:
        print('queue is empty')
    else:
        m = q.pop(0)
        print(m, 'is removed')


def display():
    print(q)


size = int(input('enter the length of queue'))
while True:
    print('1.add\n2.remove\n3.display')
    c = int(input('enter choice'))
    if c == 1:
        enqueue(size)
    elif c == 2:
        dequeue()
    else:
        display()
display()
