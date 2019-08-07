#In a doubly linked list each node contains not only the data component and
#a link to the next node as in the singly linked list
#but also a second link that points to the preceding node.

class Node():

    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class doubly_Linked_List():

    def __init__(self):
        self.head=None
        self.tail=None

    #Inserting a value into an ordered doubly linked list.
    def insert(self,data):
        newNode=Node(data)
        if self.head == None:         #empty list
            self.head=newNode
            self.tail=newNode
        elif data < self.head.data:      #insert before head
            newNode.next=self.head
            self.head.prev=newNode
            self.head=newNode
        elif data > self.tail.data:          #insert after tail
            newNode.prev=self.tail
            self.tail.next=newNode
            self.tail=newNode
        else:
            node=self.head
            while node is not None and node.data < data:
                node=node.next
            newNode.next=node
            newNode.prev=node.prev
            node.prev.next=newNode
            node.prev=newNode

    def reverseTraversal(self,tail):
        current_node= tail
        while current_node is not None:
            print(current_node.data)
        current_node=current_node.prev

    #searching a sorted doubly linked list using the probing technique.
    def search(self,target):
        if head is None:
            return False
        elif probe is None:          #initialize probe to the first node.
            probe=head
        if target < probe.data:
            while probe is not None and target <= probe.data :
                if target==probe.data:
                    return True
                else:
                    probe=probe.prev
        else:
            while probe is not None and target >= probe.data:
                if target==probe.data :
                    return True
                else:
                    probe=probe.next
        #If the target is not found in the list.
        return False
