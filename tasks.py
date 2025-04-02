def stringify(node):
    res = ''
    while node:
        res += str(node.data) + ' -> '
        node = node.next
    res += 'None'
    return res