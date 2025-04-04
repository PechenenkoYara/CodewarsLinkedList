
class Node:
    def __init__(self, data, next=None): 
        self.data = data
        self.next = next

class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

def push(head, data):
    node = Node(data)
    node.next = head
    return node

def move_node(source, dest):
    dest = push(dest, source.data)
    source = source.next
    return Context(source, dest)

