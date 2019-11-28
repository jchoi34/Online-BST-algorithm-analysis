from Binary_Search_Tree import *
from Node import *

class DynamicMonotoneTree(BinarySearchTree):
    # rotate upwards function for DM trees
    def rotate_up(self, node):
        parent = node.parent
        cost = 0
        while(node is not self.root and node.counter > parent.counter):
            if node is parent.left:
                self.rotate_right(node.parent)
            else:
                self.rotate_left(node.parent)
            cost += 1
            parent = node.parent

        return cost


    # search in DM tree
    def dmt_search(self, val):
        node, node_parent, cost = self.search(val)
        rotate_cost = 0
        if node:
            if node is not self.root:
                node.counter += 1
                rotate_cost = self.rotate_up(node)
        elif node_parent is not self.root:
            node_parent.counter  += 1
            rotate_cost = self.rotate_up(node_parent)

        return cost + rotate_cost


    # insert into DM tree
    def dmt_insert(self, node, increment=True):
        self.insert(node)
        if increment:
            node.counter += 1
            self.rotate_up(node)


    # Create a DM tree with keys
    def generate_dmt_tree(self, keys):
        self.root = DmtNode(keys[0])
        for i in keys[1:]:
            self.dmt_insert(DmtNode(i), increment=False)