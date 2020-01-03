class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def preorder_traverse(node):
    if node == None:
        return
    print(node.data, end = "->")
    preorder_traverse(node.left)
    preorder_traverse(node.right)

def inorder_traverse(node):
    if node == None:
        return
    inorder_traverse(node.left)
    print(node.data, end="->")
    inorder_traverse(node.right)

def postorder_traverse(node):
    if node == None:
        return
    postorder_traverse(node.left)
    postorder_traverse(node.right)
    print(node.data, end="->")

root = None

def init_tree():
    global root
    root = Node("A")
    root.left = Node("B")
    root.right = Node("C")
    node = root.left
    node.left = Node("D")
    node.right = Node("E")
    node = root.right
    node.left = Node("F")
    node.right = Node("G")
    
def levelorder_traverse(node):
    levelq = []
    levelq.append(node)
    while len(levelq) != 0:
        visit_node = levelq.pop(0)
        print(visit_node.data, end="->")
        if visit_node.left != None:
            levelq.append(visit_node.left)
        if visit_node.right != None:
            levelq.append(visit_node.right)

if __name__=='__main__':
    init_tree()
    print("<Preorder Traverse>")
    preorder_traverse(root)
    print("\n")
    print("<inorder Traverse>")
    inorder_traverse(root)
    print("\n")
    print("<Post Traverse>")
    postorder_traverse(root)
    print("\n")
    print("<Levelorder Traverse>")
    levelorder_traverse(root)
    print("\n")