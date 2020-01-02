class Node:
    def __init__(self, data, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

def init_list():
    global node_A
    node_A = Node("A")
    node_B = Node("A")
    node_D = Node("A")
    node_E = Node("A")
    node_A.next = node_B
    node_B.prev = node_A
    node_B.next = node_D
    node_D.prev = node_B
    node_D.next = node_E

def insert_node(data):
    global node_A
    new_node = Node(data)
    node_P = node_A
    node_T = node_A
    while node_T.data <= data:
        node_P = node_T
        node_T = node_T.next
    new_node.next = node_T
    node_P.next = new_node

def print_list():
    global node_A
    node = node_A
    while node:
        print(node)
        node = node.next
    print

if __name__ == '__main__':
    print("Link")
    init_list()
    print_list()