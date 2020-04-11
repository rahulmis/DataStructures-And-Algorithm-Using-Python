# create a class as stack name
class Stack:
    def __init__(self):
        self.arr = []
    # creating a function for push operation
    def push(self,data):
        self.arr.append(data)
    # for ckeck the stack is empty or not
    def is_empty(self):
        return self.arr == []
    # for pop operation from the stack
    def pop(self):
        if self.is_empty():
            print('Stack Is empty')
        else:
            self.arr.pop()
    # for getting peek value
    def peek(self):
        if self.is_empty():
            print('Satck Is Empty')
        else:
            return self.arr[-1]
    # return the stack
    def retstack(self):
        return self.arr
# creating a object of stack class
ob1 = Stack()
# push item in stack
ob1.push(1)
ob1.push(2)
ob1.push(3)
res = ob1.retstack()
print('After Pushing 3 elements in stack :',res)
res = ob1.is_empty()
print('Stack is empty or not : ',res)
ob1.pop()
res = ob1.retstack()
print('After Pop 1 elements in stack :',res)
res = ob1.peek()
print('Peek element of stack : ',res)
