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