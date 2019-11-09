class ListNode:
    def __init__(self, data = 0, next_node = None):
        self.data = data
        self.next = next_node

def search(L, key):
    while L and L.data != key:
        L = L.next
    return L

def insert_node(node, new_node):
    new_node.next = node.next
    node.next = new_node

def delete(node):
    node.next = node.next.next
