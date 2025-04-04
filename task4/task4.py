class Node:
    def __init__(self, data, next=None): 
        self.data = data
        self.next = next
        
def get_nth(node, index):
    if node is None:
        raise ValueError("List is empty.")
    if index < 0:
        raise ValueError("Index must be non-negative.")
    for i in range(index): 
        if node.next is None:  
            raise ValueError("Index out of range.")
        node = node.next  
    return node