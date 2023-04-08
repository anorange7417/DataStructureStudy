class Stack:
    def __init__(self):
        self.container = list()
    
    def empty(self):
        if self.container:
            return False
        else:
            return True

    def push(self,data):
        self.container.append(data)

    def pop(self):
        if self.empty():
            return
        else:
            return self.container.pop()

    def peek(self):
        if self.empty():
            return
        else:
            return self.container[-1]

mystack = Stack()
mystack.push(1)
mystack.push(2)
mystack.push(3)
while not mystack.empty():
    print(mystack.pop(), end = " ")