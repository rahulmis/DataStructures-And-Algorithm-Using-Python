######### This is a intro of  Linked list where we will discuss how Linked List Works and how to create #head and nodes and how to connect them with each other the whole implementation of Linked list is in #the next Post. You can get the implementation video on Youtube> ForCodeCoder channel name.





#######################   Create a Node class which will create data and next 
class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

##--------------------- Create Linked List Class where we will define a head in constructure
class LinkedList:
    def __init__(self):
        self.head = None
#------make a object of LinkedList class
ob1 = LinkedList()
#----------------------------- after making a object of LinkedlIst Calss The Constructure Will
# create a head and the value of head is None now create a Call The Node Class and the Constructure of
# Node class will create 2 objects which is data and next the 15 will assign in data and next is None

ob1.head = Node(15)

# create a second name variabel that will store address of Node(3) where data = 3 and next = None

second = Node(3)

# create a third name variabel that will store address of Node(17) where data = 17 and next = None

third = Node(17)

# create a fourth name variabel that will store address of Node(90) where data = 90 and next = None

fourth = Node(90)


# now we are going the create a link and connect all the nodes with each other manually
# we know that ob1.head contains NOne value so in the place of None we will assign the address of second 
# node and in the second.next assign third and third.next assign fourth

ob1.head.next = second
second.next = third
third.next = fourth
print(ob1.head.next.next.next.data)