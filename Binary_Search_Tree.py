from Node import *

class BinarySearchTree:
    def __init__(self, root=None):
        self.root = root


    # Search a bst
    def search(self, val):
        if (self.root is None):
            return None, None, 0
        cost = 1
        temp_parent = None
        temp = self.root
        while (temp and temp.val != val):
            temp_parent = temp
            if (val < temp.val):
                temp = temp.left
            else:
                temp = temp.right
            cost += 1

        return temp, temp_parent, cost  # may return None, None, cost


    # calculate the depth of a node
    def depth(self, val):
        if (self.root is None):
            return 0
        depth = 0
        temp = self.root
        while (temp and temp.val != val):
            if (val < temp.val):
                temp = temp.left
            else:
                temp = temp.right
            depth += 1

        return depth if temp else 0


    # Insert into a bst
    def insert(self, node):
        if node is None:
            return
        if self.root is None:
            self.root = node
            return
        temp_parent = None
        temp = self.root
        while (temp):
            temp_parent = temp
            if (node.val <= temp.val):
                temp = temp.left
            else:
                temp = temp.right

        node.parent = temp_parent
        if (node.val <= temp_parent.val):
            temp_parent.left = node
        else:
            temp_parent.right = node


    # Delete from a bst
    def delete(self, node):
        '''
        Same algorithm from CLRS textbooks.

        :param root: root of tree
        :param node: node to delete
        '''

        if self.root is None or node is None or (self.root is not node and node.parent is None):
            return
        if node.left is None:
            self.transplant(node, node.right)
        elif node.right is None:
            self.transplant(node, node.left)
        else:
            successor = tree_min(node.right)
            if successor.parent is not node:
                self.transplant(self.root, successor, successor.right)
                successor.right.parent = successor
            self.transplant(self.root, node, successor)
            successor.left = node.left
            successor.left.parent = successor
        del node


    def rotate_right(self, node):
        '''
        Right rotate function from CLRS textbook.

        :param root: root of tree
        :param node: node to rotate
        '''

        y = node.left
        node.left = y.right
        if y.right:
            y.right.parent = node
        y.parent = node.parent
        if node.parent is None:
            self.root = y
        elif node is node.parent.left:
            node.parent.left = y
        else:
            node.parent.right = y
        y.right = node
        node.parent = y


    def rotate_left(self, node):
        '''
        Left rotate function from CLRS textbook.

        :param root: root of tree
        :param node: node to rotate
        '''

        y = node.right
        node.right = y.left
        if y.left:
            y.left.parent = node
        y.parent = node.parent
        if node.parent is None:
            self.root = y
        elif node is node.parent.left:
            node.parent.left = y
        else:
            node.parent.right = y
        y.left = node
        node.parent = y


    def transplant(self, u, v):
        '''
        Helper for delete(root, node) to move subtrees.
        Same algorithm from CLRS textbooks.

        :param root: root of tree
        :param u: node to move
        :param v: node to take u's place
        '''

        if self.root is u:
            self.root = v
        elif u is u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v:
            v.parent = u.parent


    # Return smallest element in a tree
    def tree_min(self, node):
        while node.left:
            node = node.left

        return node


    # Create a BST with keys
    def generate_bst(self, keys):
        self.root = Node(keys[0])
        for i in keys[1:]:
            self.insert(Node(i))

        return self.root


    # Display elements of a tree in order
    def in_order_traversal(self, node):
        if node:
            self.in_order_traversal(node.left)
            print(node.val)
            self.in_order_traversal(node.right)