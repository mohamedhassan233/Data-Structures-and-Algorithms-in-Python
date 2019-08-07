#A priority queue is a queue in which each item is assigned a priority
#and items with a higher priority are removed before those with a lower priority

#associating queue items with their priority.
class PriorityStorage(object):

    def __init__(self, item, priority):
        self.item=item
        self.priority=priority

#Implementation of the unbounded Priority Queue using a list
#new items appended to the end.
class PriorityQueue():

    def __init__(self):
        self.queue=[]

    def isEmpty(self):
        return len(self.queue)==0    #Returns True if the queue is empty.

    def length(self):         #Returns the number of items in the queue.
        return len(self.queue)

    def enqueue(self, item, priority):      #Adds the given item to the queue.
        new=PriorityStorage(item, priority)
        self.queue.append(new)

    def dequeue(self):
        if self.isEmpty():
            raise IndexError("Can not dequeue from an empty queue.")
        highest=self.queue[i].priority        #highest priority (smallest integer).
        for i in range(self.length()):
            if self.queue[i].priority < highest:
                highest=self.queue[i].priority
        #Remove the element with the highest priority and return it.
        removed=self.queue.pop(highest)
        return removed.item

