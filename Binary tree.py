#binary tree is a tree where each node has most two children
#often referred to the left and right children

class BinaryTree():

    def __init__(self,data):
        self.root = data
        self.left = None
        self.right = None

    def insertLeft(self,data):
        if self.left == None:
            self.left = BinaryTree(data)
        else:
            newNode = BinaryTree(data)
            node.left = self.left
            self.left = newNode

    def insertRight(self,data):
        if self.right == None:
            self.right = BinaryTree(data)
        else:
            newNode = BinaryTree(data)
            newNode.right= self.right
            self.right = newNode

    def getRightChild(self):
        return self.right

    def getLeftChild(self):
        return self.left

    def setRootValue(self,data):
        self.root = data

    def getRootValue(self):
        return self.root

