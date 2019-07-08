#when you add an item to a stack, you place it on top of the stack
#when you remove an item from the stack, you always remove the topmost item

class stack():

    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return self.items==[]

    def push(self,item):                    #adding an element to the top of the stack
        self.items.append(item)

    def pop(self):                          #removing the top element of the stack
        if  not self.items:
            return  None
        return self.items.pop()

    def peek(self):                         #return the item from the top of stack without removing it
        if  not self.items:
            return  None
        return self.items[-1]

    def size(self):
        return  len(self.items)



#Queues maintain the order of your elements to process later

class queue():

    def __init__(self):
        self.queue=[]

    def isEmpty(self):
        return self.queue==[]

    def enqueue(self,data):                 #insert an element at the back of the queue
        self.queue.append(data)

    def dequeue(self):                      #remove the element at the front of the queue
        if not self.queue :
            return None
        return self.queue.pop(0)

    def peek(self):                         #return the element at the front of the queue
        if not self.queue :
            return None
        return self.queue[0]

    def size(self):
        return len(self.queue)



#Balanced parentheses means that each opening symbol
#has a corresponding closing symbol and the pairs of
#parentheses are properly nested

def BalancedParentheses(string):
    s=stack()
    balance=1
    index =0
    while index<len(string) and balance:
        sympol=string[index]
        if sympol=='(':
            s.push(sympol)
        else:
            if s.isEmpty():
                balance=0
            else:
                s.pop()

        index+=1

    if balance and s.isEmpty():
        return True
    else:
        return False


#palindrome is a string that reads the same forward and backward

def Palindrome(string):
    word=queue()
    for ch in string:
        word.enqueue(ch)
    
    check=True

    while check and word.size()>1:
        first=word.dequeue()
        last=word.removeRear()
        if last != first:
            check=False

    return check
