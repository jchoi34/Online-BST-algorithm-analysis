from Binary_Search_Tree import *
from Node import *

class SingleRotateTree(BinarySearchTree):
    # single rotate function for trees using Single Rotate (SR) heuristic
    def single_rotate(self, node):
        parent = node.parent
        if node is parent.left:
            self.rotate_right(node.parent)
        else:
            self.rotate_left(node.parent)


    # search in SR tree
    def srt_search(self, val):
        node, node_parent, cost = self.search(val)
        if node:
            if node is not self.root:
                self.single_rotate(node)
                cost += 1
        elif node_parent is not self.root:
            self.single_rotate(node_parent)
            cost += 1

        return cost


    # insert into splay tree
    def srt_insert(self, node):
        self.insert(node)
        self.single_rotate(node)


    # Create a splay tree with keys
    def generate_srt(self, keys):
        self.root = Node(keys[0])
        for i in keys[1:]:
            self.srt_insert(Node(i))