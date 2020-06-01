"""
1 = Inorder = (left root right)
2 = preorder = ( root left right)
3 = postorder = (left right  root)


     1  first.left.left.data
    / \
   2   3
 / \  / \
4  5 6   7


"""
class node:
    def __init__(self,data=None):
        self.data = data
        self.left_node = None
        self.right_node = None
class BinaryTree:
    def __init__(self):
        self.root = None

ob1 = BinaryTree()
first = node(1)
second = node(2)
third = node(3)
fourth = node(4)
fifth = node(5)
sixth = node(6)
seventh = node(7)
ob1.root = first
first.left_node = second
first.right_node = third
second.left_node = fourth
second.right_node = fifth
third.left_node = sixth
third.right_node = seventh
