class Node:
    def __init__(self, data=None):
        self.__data = data
        self.__prev = None
        self.__next = None
    def __del__(self):
        print("data of {} is deleted".format(self.data))
    
    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, data):
        self.__data = data
    
    @property
    def prev(self):
        return self.__prev
    
    @prev.setter
    def prev(self, data):
        self.__prev = data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, data):
        self.__next = data

class DoubleLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.d_size = 0
    def empty(self):
        if self.d_size == 0:
            return True
        else:
            return False
    def size(self):
        return self.d_size
    def add_first(self,data):
        # YOU SHOULD DEFINE NEW NODE FIRST
        new_node = Node(data)
        new_node.next = self.head.next
        new_node.prev = self.head
        # THEN YOU MODIFY NEW NODE'S NEXT NODE(THIS TIME, IT'S HEAD'S NEXT NODE)'S PREVIOUS NODE AS NEW NODE
        self.head.next.prev = new_node
        # THEN MODIFY NEW NODE'S PREVIOUS NODE(THIS TIME, IT IS HEAD NODE)'S NEXT NODE AS NEW NODE
        self.head.next = new_node
        self.d_size += 1

    def add_last(self,data):
        new_node = Node(data)
        new_node.next = self.tail
        new_node.prev = self.tail.prev
        self.tail.prev.next = new_node
        self.tail.prev = new_node
        self.d_size += 1

    def insert_after(self, data, node):
        new_node = Node(data)
        new_node.prev = node
        new_node.next = node.next
        node.next.prev = new_node
        node.next = new_node
        self.d_size += 1
    
    def insert_before(self, data, node):
        new_node = Node(data)
        new_node.prev = node.prev
        new_node.next = node
        node.prev.next = new_node
        node.prev = new_node
        self.d_size += 1
    
    def search_forward(self, target):
        cur = self.head.next
        while cur is not target:
            if cur.data == target:
                return cur
            cur = cur.next
        return None

    def search_backward(self, target):
        cur = self.tail.prev
        while cur is not target:
            if cur.data == target:
                return cur
            cur = cur.prev
        return None

    def delete_first(self):
        if self.empty():
            return
        self.head.next = self.head.next.next
        self.head.next.prev = self.head
        self.d_size -= 1

    def delete_last(self):
        if self.empty():
            return
        self.d_size -= 1
        self.tail.prev = self.trail.prev.prev
        self.tail.prev.next = self.tail
    
    def delete_node(self,node):
        if self.empty():
            return
        self.d_size -= 1
        node.prev.next = node.next
        node.next.prev = node.prev

    def show(self):
        if self.d_size == 0:
            print("your list is empty")
            return
        cur = self.head.next
        while cur is not self.tail:
            print(cur.data, end = " ")
            cur = cur.next
        print()

mylist = DoubleLinkedList()
print(mylist.d_size)
mylist.add_last(1)
mylist.add_last(2)
mylist.add_last(3)
mylist.add_last(5)
mylist.insert_after(4,mylist.search_forward(5))
mylist.insert_before(6,mylist.search_backward(5))
mylist.delete_node(mylist.search_backward(5))
mylist.show()
