class Node:
    def __init__(self,data= None,next=None):
        self.data = data
        self.next = next
class Linked_List:
    def __init__(self):
        self.head = None
    def traverse(self):  # 321
        temp = self.head
        while temp:
            print(temp.data,'->', end= ' ')
            temp = temp.next
        print(temp)
    def addstart(self,data):
        self.head = Node(data=data,next=self.head)
    def addend(self,data):
        New_Node = Node(data=data)
        if(self.head == None):
            self.head = New_Node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = New_Node
    def length(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        print("Linked List Length = {}".format(count))
    def addgivenpos(self,data,pos):
        New_Node = Node(data=data)
        if(self.head == None):
            print("Linked List Is Empty...")
        else:
            temp = self.head
            cc = -1
            while temp:
                if(cc == pos-2):
                    tt = temp.next
                    temp.next = New_Node
                    New_Node.next = tt
                else:
                    temp = temp.next
                cc += 1
    def deletestart(self):
        if(self.head == None):
            print("Linked List Is Empty So Deletion is Not Possible...")
        else:
            self.head = self.head.next
    def deleteend(self):
        if(self.head == None):
            print("Linked List Is Empty So Deletion is Not Possible...")
        else:
            temp = self.head
            while temp.next.next:
                temp = temp.next
            temp.next = None
    def emptylinkedlist(self):
        self.head = None

ob1 = Linked_List()
ob1.addstart(1)
ob1.addstart(2)
ob1.addstart(3)
ob1.addstart(4)
ob1.traverse()
ob1.addend(5)
ob1.addend(6)
ob1.addend(7)
ob1.traverse()
ob1.length()
ob1.addgivenpos(0,4)
ob1.traverse()
ob1.deletestart()
ob1.deletestart()
ob1.traverse()
# ob1.deleteend()
# ob1.deleteend()
# ob1.deleteend()
# ob1.deleteend()
# ob1.deleteend()
ob1.traverse()
ob1.emptylinkedlist()
ob1.traverse()