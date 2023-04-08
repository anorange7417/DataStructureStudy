class Qeueue:
    def __init__(self):
        self.container = list()

    def empty(self):
        if not self.container:
            return True
        else:
            return False

    def enqueue(self, data):
        self.container.append(data)

    def dequeue(self):
        return self.container.pop(0)

    def peek(self):
        return self.container[0]

q = Qeueue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.dequeue()
while not q.empty():
    print(q.dequeue(), end = " ")