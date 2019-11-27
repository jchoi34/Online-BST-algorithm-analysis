from Binary_Search_Tree import *

class DMT_Node(Node):
    def __init__(self, val=-1, parent=None, counter=0):
        super().__init__(val, parent)
        self.counter = counter


# rotate upwards function for DM trees
def rotate_up(root, node):
    parent = node.parent
    cost = 0
    while(node is not root and node.counter > parent.counter):
        if node is parent.left:
            root = rotate_right(root, node.parent)
        else:
            root = rotate_left(root, node.parent)
        cost += 1
        parent = node.parent

    return root, cost


# search in DM tree
def dmt_search(root, val):
    node, node_parent, cost = search(root, val)
    rotate_cost = 0
    if node:
        if node is not root:
            node.counter += 1
            root, rotate_cost = rotate_up(root, node)
    elif node_parent is not root:
        node_parent.counter  += 1
        root, rotate_cost = rotate_up(root, node_parent)

    return root, cost + rotate_cost


# insert into DM tree
def dmt_insert(root, node, increment=True):
    insert(root, node)
    if increment:
        node.counter += 1
        root = rotate_up(root, node)

    return root


# Create a DM tree with keys
def generate_dmt_tree(keys):
    tree = DMT_Node(keys[0])
    for i in keys[1:]:
        tree = dmt_insert(tree, DMT_Node(i), increment=False)

    return tree


# test
def test():
    tree = generate_dmt_tree([5, 1, 2, 3, 4])
    tree.display()
    print()
    tree = dmt_search(tree, 4)
    tree.display()
    print()
    tree = dmt_search(tree, 5)
    tree.display()
    print()
    tree = dmt_search(tree, 5)
    tree.display()
    print()
    tree = dmt_search(tree, 2)
    tree.display()
    print()
    tree = dmt_insert(tree, DMT_Node(6))
    tree.display()
    print()
    tree = dmt_search(tree, 2)
    tree.display()
    print()
    tree = dmt_search(tree, 2)
    tree.display()
    print()