class Queue:
    def __init__(self):
        self.arr = []
    def enque(self,data):
        self.arr.insert(0,data)
    def deque(self):
        if(len(self.arr)!=0):
            self.arr.pop()
        else:
            print("Queue Is empty : ")
    def traverse(self):
        if(len(self.arr)!=0):
            for i in self.arr:
                print(i,end=' ')
            print()
        else:
            print("Queue Is empty : ")
    def is_empty(self):
        if(len(self.arr)==0):
            print('True')
        else:
            print("False")
    def peek(self):
        if(len(self.arr)!=0):
            print(self.arr[-1])
        else:
            print("Queue Is empty : ")
    def front(self):
        if(len(self.arr)!=0):
            print(self.arr[-1])
        else:
            print("Queue Is empty : ")
    def rear(self):
        if(len(self.arr)!=0):
            print(self.arr[0])
        else:
            print("Queue Is empty : ")

ob1 = Queue()
for i in range(10):
    ob1.enque(i)
ob1.traverse()
ob1.peek()
ob1.is_empty()
ob1.deque()
ob1.traverse()
ob1.enque(10)
ob1.traverse()
ob1.front()
ob1.rear()