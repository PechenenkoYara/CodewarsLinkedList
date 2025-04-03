class Node:
    def __init__(self, data, next=None): 
        self.data = data
        self.next = next
        
def stringify(node):
    res = ''
    while node:
        res += str(node.data) + ' -> '
        node = node.next
    res += 'None'
    return res


def linked_list_from_string(s):
    values = [int(x) for x in s.split(" -> ") if x != "None"]
    head = None
    current = None
    for value in values:
        if head is None:
            head = Node(value)
            current = head
        else:
            current.next = Node(value)
            current = current.next
    return head



def push(head, data):
    node = Node(data)
    node.next = head
    return node

def build_one_two_three():
    head = None
    head = push(head, 3)
    head = push(head, 2)
    head = push(head, 1)
    return head

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

class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest
    
def move_node(source, dest):
    dest = push(dest, source.data)
    source = source.next
    return Context(source, dest)


def sorted_insert(head, data):
    new_node = Node(data)
    if head is None or data < head.data:
        new_node.next = head
        return new_node
    current = head
    while current.next is not None and current.next.data < data:
        current = current.next
    new_node.next = current.next
    current.next = new_node
    return head

def reverse(head):
    if head is None:
        return head
    new_list = Node(head.data)
    while head.next is not None:
        head = head.next
        new_list = push(new_list, head.data)
    return new_list