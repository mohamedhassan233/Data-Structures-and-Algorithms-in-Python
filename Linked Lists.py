#linked list consists of nodes where each node contains a data field
#and a reference to the next node in the list.

class Node(object):

    def __init__(self,data):
        self.data=data
        self.next=None

#insertion & deletion methods of linked list

class LinkedList(object):

    def __init__(self):
        self.head =None
        self.size=0

    def push(self,data):             #inserting items at the beginning of the linked list
        self.size+=1
        newNode=Node(data)
        if not self.head:
            self.head= newNode
        else:
            newNode.next=self.head
            self.head=newNode

    def size(self):
        return self.size

    def length(self):                       #iterate whole linked list to calculate how many items stored
        current_node = self.head
        length=0
        while current_node is not None:
            length+=1
            current_node=current_node.next
        return length

    def append(self,data):                  #inserting items at the End of the linked list
        self.size+=1
        newNode=Node(data)
        if self.head is None :
            self.head=newNode
        current_node=self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next=newNode

    def insertAfter(self,previousNode,data):               #inserting item after particular node of the list
        current_node=self.head
        while current_node is not None:
            if (current_node.data) == (previousNode):
                break
            current_node=current_node.next
        if current_node is None:
            print("item not in the list")
        else:
            self.size+=1
            newNode=Node(data)
            newNode.next=previousNode.next     #Make next of new data as next of previous Node
            previousNode.next=newNode

    def printNodes(self):                   #print the All linked list
        current_node = self.head
        if current_node is None :
            return None
        while (current_node is not None):
            print (self.data)
            current_node = current_node.next

    def remove(self,data):                      #deletion by the Item Value
        if self.head is None:
            return
        current_node=self.head
        if current_node.data == data:       #deleting first node
            self.head=current_node.next
            self.size-=1
            return
        current_node=self.head
        while current_node.next is not None:
            if current_node.next.data == data:
                break
            current_node=current_node.next
        if current_node.next is None:
            print("item not found in the list")
        else:
            self.size-=1
            current_node.next=current_node.next.next

    def pop(self):                          #delete the item at the front of the list
        if self.head is None :
            print("The list has no items to delete")
            return
        self.head=self.head.next

    def removeLast(self):                   #delete the item at the End of the list
        if self.head is None :
            print("The list has no items to delete")
            return
        current_node=self.head
        while current_node.next.next is not None:
            current_node=current_node.next
        current_node.next=None
        self.size-=1

    def search(self,item):
        if self.head is None :
            print("List has no items")
            return
        current_node=self.head
        while current_node is not None :
            if current_node.data == item :
                print("Item found")
                return True
            current_node=current_node.next
        print("item not found")
        return False


