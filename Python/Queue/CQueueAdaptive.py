# this is Circular Queue allowing inserting elements which their number exceed queue's maximum size 
class CQueue:
    MAXSIZE = 10
    def __init__(self):
        self.container  = [None] * CQueue.MAXSIZE
        self.front = 0
        self.rear = 0
    def is_empty(self):
        if self.front == self.rear:
            return True
        else:
            return False
    def __step_forward(self,x):
        x += 1
        if x >= CQueue.MAXSIZE:
            x = 0
        return x
    def is_full(self):
        next = self.__step_forward(self.rear)
        if next == self.front:
            return True
        return False
    def enqueue(self, data):
        if self.is_full():
            self.dequeue()
            self.container[self.rear] = data
            self.rear = self.__step_forward(self.rear)
        else:
            self.container[self.rear] = data
            self.rear = self.__step_forward(self.rear)
    def dequeue(self):
        if self.is_empty():
            raise Exception("The queue is empty")
        ret = self.container[self.front]
        self.front = self.__step_forward(self.front)
        return ret
    def peek(self):
        if self.is_empty():
            raise Exception("The queue is empty")
        return self.container[self.front]

if __name__ == '__main__':
    cq = CQueue()
    for i in range(20): # exceed its maximum size
        cq.enqueue(i)
    while not cq.is_empty():
        print(cq.dequeue(), end=" ")