#the value of the left child must be less than the value if its parent
#the value of the right child must be greater than or equal to the value of its parent

class Node():

    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        

class BinarySearchTree():

    def __init__(self):
        self.root=None

    def insert(self,data):
        if not self.root:
            self.root=Node(data)
        else:
            self.insertNode(self.root, data)

    def insertNode(self,node,data):
        if data<node.data:
            if node.left:
                self.insertNode(node.left, data)
            else:
                node.left=Node(data)
        else:
            if node.right:
                self.insertNode(node.right, data)
            else:
                node.right=Node(data)

    def removeNode(self,node,data):
        if not node:
            return node
        elif data<node.data:
            node.left=self.removeNode(node.left,data)
            return node
        elif data>node.data:
            node.right=self.removeNode(node.right,data)
            return node
        else:
            if not node.left and not node.right:                 #removing a leaf node
                del node
                return None
            elif not node.left:                    #removing a node with single right child
                temp=node.right
                del node
                return temp
            elif not node.right:                  #removing a node with single left child
                temp=node.left
                del node
                return temp
            else:                              #look for the successor and swap two nodes
                successor=self.getMin(node.right)
                node.data=successor.data
                node.right=self.removeNode(node.right, successor.data)

    def remove(self,data):
        if self.root:
            self.root=self.removeNode(self.root,data)

    def getMinValue(self):
        if self.root:
            return self.getMin(self.root)

    def getMin(self, node):
        if node is None:
            return None
        elif node.left is None:
            return node
        else:
            return self.getMin(node.left)

    def getMaxValue(self) :
        if self.root :
            return self.getMax(self.root)

    def getMax(self, node) :
        if node is None :
            return None
        elif node.right is None :
            return node
        else :
            return self.getMin(node.right)

#the inorder traversal
#we visit the left subtree + the root node + the right subtree recursively
    def inorderTraversal(self, root) :
        if root.left is not None :
            self.inorderTraversal(root.left)
        print(root.data)
        if root.right is not None:
            self.inorderTraversal(root.right)

#the preorder traversal
#we visit the root + left subtree + the right subtree recursively
    def preorderTraversal(self, root):
        print(root.data)
        if root.left is not None:
            self.preorderTraversal(root.left)
        if root.right is not None :
            self.preorderTraversal(root.right)

#the preorder traversal
#we visit the left subtree + the right subtree + the root recursively
    def postorderTraversal(self, root) :
        if root.left is not None :
            self.postorderTraversal(root.left)
        if root.right is not None :
            self.postorderTraversal(root.right)
        print(root.data)
