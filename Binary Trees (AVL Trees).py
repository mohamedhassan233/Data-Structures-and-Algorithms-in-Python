#AVL tree was invented by G. M. Adel'son-Velskii and Y. M. Landis in 1962
#improves on binary search tree by always guaranteeing the tree is height balanced

class Node():

    def __init__(self,data):
        self.data=data
        self.height=0
        self.left=None
        self.right=None


class AVL():

    def __init__(self):
        self.root=None

    def insert(self, data):
        self.root=self.insertNode(self.root, data)

    def insertNode(self, root, data):
        if not root:
            return Node(data)
        elif data < root.data:
            root.left=self.insertNode(root.left, data)
        else:
            root.right=self.insertNode(root.right, data)         #then Update the height
        root.height=max(self.height(root.left),self.height(root.right))+1
        balance=self.balance(root)                        #get the balance factor
        #rotate Cases
        if balance > 1 and data < root.left.data:
            return self.rightRotate(root)
        if balance < -1 and data > root.right.data:
            return self.rotateLeft(root)
        if balance > 1 and data > root.left.data:
            root.left=self.rotateLeft(root.left)
            return self.rotateRight(root)
        if balance < -1 and data < root.right.data:
            root.right=self.rotateRight(root.right)
            return self.rotateLeft(root)
        return root

    def height(self,root):
        if not root:
            return -1
        return root.height

    def balance(self,node):        #if return value >1 means it is left heavy tree
        if not node:                     #=> right rotation else: left rotation / right heavy
            return 0
        return self.height(node.left) - self.height(node.right)

    def rotateRight(self,root):
        temp = root.left
        (t) = temp.right
        temp.right=root            #Perform rotation
        root.left=(t)
        return temp                  #return new root
        root.height=max(self.height(root.left) , self.height(root.right))+1
        temp.height=max(self.height(temp.left) , self.height(temp.right))+1

    def rotateLeft(self,root):
        temp = root.right
        (t) = temp.left
        temp.left=root            #Perform rotation
        root.right=(t)
        return temp                  #return new root
        root.height=max(self.height(root.left) , self.height(root.right))+1
        temp.height=max(self.height(temp.left) , self.height(temp.right))+1

    def preorderTraversal(self, root):
        if not root:
            return None
        print("{0}".format(root.data), end="")
        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)

