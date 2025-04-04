class Node:
    def __init__(self, data, next=None): 
        self.data = data
        self.next = next
        
def swap_pairs(head):
    if head is None:
        return head
    start = Node(0)
    start.next = head
    current = start
    while head and head.next:
        first = head
        second = head.next
        current.next = second
        first.next = second.next
        second.next = first
        current = first
        head = first.next
    return start.next