from Binary_Search_Tree import *

# single rotate function for trees using Single Rotate (SR) heuristic
def single_rotate(root, node):
    parent = node.parent
    if node is parent.left:
        root = rotate_right(root, node.parent)
    else:
        root = rotate_left(root, node.parent)

    return root


# search in SR tree
def srt_search(root, val):
    node, node_parent, cost = search(root, val)
    if node:
        if node is not root:
            root = single_rotate(root, node)
            cost += 1
    elif node_parent is not root:
        root = single_rotate(root, node_parent)
        cost += 1

    return root, cost


# insert into splay tree
def srt_insert(root, node):
    insert(root, node)
    root = single_rotate(root, node)

    return root


# Create a splay tree with keys
def generate_srt(keys):
    tree = Node(keys[0])
    for i in keys[1:]:
        tree = srt_insert(tree, Node(i))

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
    root = srt_search(root, 5)
    root.display()
    print()
    root = srt_insert(root, node2)
    root.display()
    print()
    root = srt_search(root, 5)
    root.display()
    print()
    root = srt_insert(root, node3)
    root.display()
    print()
    root = srt_insert(root, node1)
    root.display()
    print()
    root = srt_search(root, 3)
    root.display()
    print()
    root = srt_insert(root, node4)
    root.display()
    print()
    root = srt_search(root, 5)
    root.display()
    print()
    root = srt_search(root, 5)
    root.display()
    print()