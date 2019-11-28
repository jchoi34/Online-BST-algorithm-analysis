from Binary_Search_Tree import *
from Node import *

class SplayTree(BinarySearchTree):
    # Splay function for splay trees
    def splay(self, node):
        cost = 0
        while(self.root is not node):
            parent = node.parent
            if parent is self.root:  # Zig
                cost += 1
                if node is self.root.left:  # left path
                    self.rotate_right(node.parent)
                else:  # right path
                    self.rotate_left(node.parent)
                return cost
            # Only set root to new reference on 2nd rotate because a splayed node can only become the root after
            # the 2nd rotate here. If the splayed node is not the root after 2nd rotate the same
            # reference for root will be returned.
            elif node is parent.left and parent is parent.parent.left:  # Zig-Zig grandchild is on left left path
                self.rotate_right(parent.parent)
                self.rotate_right(node.parent)
            elif node is parent.right and parent is parent.parent.right:  # Zig-Zig grandchild is on right right path
                self.rotate_left(parent.parent)
                self.rotate_left(node.parent)
            elif node is parent.left and parent is parent.parent.right:  # Zig-Zag grandchild is on left right path
                self.rotate_right(node.parent)
                self.rotate_left(node.parent)
            elif node is parent.right and parent is parent.parent.left:  # Zig-Zag grandchild is on right left path
                self.rotate_left(node.parent)
                self.rotate_right(node.parent)
            cost += 2

        return cost


    # search in splay tree
    def splay_search(self, val):
        node, node_parent, cost = self.search(val)
        if node:
            if node is not self.root:
                cost += self.splay(node)
            return cost
        elif node_parent is not root:
            cost += self.splay(node_parent)
        return cost


    # insert into splay tree
    def splay_insert(self, node):
        self.insert(node)
        self.splay(node)


    # Create a splay tree with keys
    def generate_splay_tree(self, keys):
        self.root = Node(keys[0])
        for i in keys[1:]:
            self.splay_insert(Node(i))