class Node:
    """
    AN object for storing a singel node of a linked list. 
    Models two attributes - data and the link to the next node in the list
    """ 
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<Node data: %s" % self.data
    
class LinkedList:
    """
    Singly Linked List
    """
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None
    
    def size(self):
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node
        return count