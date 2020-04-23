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
print("After enque 1 to 10 :> ",end='')
ob1.traverse()
print("Peek Valuue Of Queue :> ",end='')
ob1.peek()
print("Queue is Empty Or NOt ? :> ",end='')
ob1.is_empty()
ob1.deque()
print("After Deque :> ",end='')
ob1.traverse()
ob1.enque(10)
print("After enque 10  :> ",end='')
ob1.traverse()
print('Front Of Queue :> ',end='')
ob1.front()
print('Rear Of Queue :> ',end='')
ob1.rear()