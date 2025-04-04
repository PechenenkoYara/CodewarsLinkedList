class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
        
def alternating_split(head):
    if head is None:
        raise ValueError("Input list cannot be None")
    if head.next is None:
        raise ValueError("Input list cannot be None")

    a_head = a_tail = None
    b_head = b_tail = None
    turn = True 

    current = head

    while current:
        next_node = current.next
        current.next = None 
        if turn:
            if a_head is None:
                a_head = a_tail = current
            else:
                a_tail.next = current
                a_tail = current
        else:
            if b_head is None:
                b_head = b_tail = current
            else:
                b_tail.next = current
                b_tail = current
        turn = not turn
        current = next_node
    return Context(a_head, b_head)