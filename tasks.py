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