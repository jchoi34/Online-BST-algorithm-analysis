from Binary_Search_Tree import *

# Splay function for splay trees
def splay(root, node):
    cost = 0
    while(root is not node):
        parent = node.parent
        if parent is root:  # Zig
            cost += 1
            if node is root.left:  # left path
                rotate_right(root, node.parent)
            else:  # right path
                rotate_left(root, node.parent)
            return cost
        # Only set root to new reference on 2nd rotate because a splayed node can only become the root after
        # the 2nd rotate here. If the splayed node is not the root after 2nd rotate the same
        # reference for root will be returned.
        elif node is parent.left and parent is parent.parent.left:  # Zig-Zig grandchild is on left left path
            rotate_right(root, parent.parent)
            root = rotate_right(root, node.parent)
        elif node is parent.right and parent is parent.parent.right:  # Zig-Zig grandchild is on right right path
            rotate_left(root, parent.parent)
            root = rotate_left(root, node.parent)
        elif node is parent.left and parent is parent.parent.right:  # Zig-Zag grandchild is on left right path
            rotate_right(root, node.parent)
            root = rotate_left(root, node.parent)
        elif node is parent.right and parent is parent.parent.left:  # Zig-Zag grandchild is on right left path
            rotate_left(root, node.parent)
            root = rotate_right(root, node.parent)
        cost += 2

    return cost


# search in splay tree
def splay_search(root, val):
    node, node_parent, cost = search(root, val)
    if node:
        if node is not root:
            cost += splay(root, node)
        return node, cost
    elif node_parent is not root:
        cost += splay(root, node_parent)
    return node_parent, cost


# insert into splay tree
def splay_insert(root, node):
    insert(root, node)
    splay(root, node)

    return node


# Create a splay tree with keys
def generate_splay_tree(keys):
    tree = Node(keys[0])
    for i in keys[1:]:
        tree = splay_insert(tree, Node(i))

    return tree


# test
def test():
    node5 = Node(5)
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    print('Root')
    root = node5
    root = splay_search(root, 5)
    root.display()
    print()
    root = splay_insert(root, node2)
    root.display()
    print()
    root = splay_search(root, 5)
    root.display()
    root = splay_insert(root, node3)
    root.display()
    print()
    root = splay_search(root, 5)
    root.display()
    print()
    root = splay_search(root, 2)
    root.display()
    print()
    root = splay_search(root, 5)
    root.display()
    print()
    root = splay_insert(root, node1)
    root.display()
    print()
    root = splay_search(root, 2)
    root.display()
    print()
    root = splay_search(root, 3)
    root.display()
    print()
    root = splay_insert(root, node4)
    root.display()
    print()
    root = splay_search(root, 0)
    root.display()

    print('Elemnts in order')
    in_order_traversal(root)