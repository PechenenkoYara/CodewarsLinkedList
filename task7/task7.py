class Node:
    def __init__(self, data, next=None): 
        self.data = data
        self.next = next


def push(head, data):
    node = Node(data)
    node.next = head
    return node

def reverse(head):
    if head is None:
        return head
    new_list = Node(head.data)
    while head.next is not None:
        head = head.next
        new_list = push(new_list, head.data)
    return new_list