class Node:
    def __init__(self, data, next=None): 
        self.data = data
        self.next = next
        

def remove_duplicates(head):
    if head is None:
        return head
    lst = {head.data}
    current = head
    while current.next is not None:
        if current.next.data in lst:
            current.next = current.next.next
        else:
            lst.add(current.next.data)
            current = current.next
    return head
