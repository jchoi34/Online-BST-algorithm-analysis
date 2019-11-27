# Tree node
class Node:
    def __init__(self, val=-1, parent=None):
        self.parent = parent
        self.left = None
        self.right = None
        self.val = val


    def __str__(self):
        return str(self.val)


    '''
    THIS DISPLAY FUNCTION IS NOT MINE!!!!!!!
    It is from the url below.

    https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python
    By user: https://stackoverflow.com/users/1143396/j-v
    '''

    def display(self):
        lines, _, _, _ = self._display_aux()
        for line in lines:
            print(line)

    '''
    THIS DISPLAY FUNCTION IS NOT MINE!!!!!!!
    It is from the url below.

    https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python
    By user: https://stackoverflow.com/users/1143396/j-v
    '''

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.val
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.val
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.val
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.val
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


# Search a bst
def search(root, val):
    if (root is None):
        return None, None, 0

    cost = 1
    temp_parent = None
    temp = root
    while (temp and temp.val != val):
        temp_parent = temp
        if (val < temp.val):
            temp = temp.left
        else:
            temp = temp.right
        cost += 1

    return temp, temp_parent, cost  # may return None, None, cost


# calculate the depth of a node
def depth(root, val):
    if (root is None):
        return 0

    depth = 0
    temp = root
    while (temp and temp.val != val):
        if (val < temp.val):
            temp = temp.left
        else:
            temp = temp.right
        depth += 1

    return depth if temp else 0


# Insert into a bst
def insert(root, node):
    if (root is None or node is None):
        return

    temp_parent = None
    temp = root
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

    return root


# Delete from a bst
def delete(root, node):
    '''
    Same algorithm from CLRS textbooks.

    :param root: root of tree
    :param node: node to delete
    '''

    if root is None or node is None or (root is not node and node.parent is None):
        return root

    if node.left is None:
        root = transplant(root, node, node.right)
    elif node.right is None:
        root = transplant(root, node, node.left)
    else:
        successor = tree_min(node.right)
        if successor.parent is not node:
            root = transplant(root, successor, successor.right)
            successor.right.parent = successor
        root = transplant(root, node, successor)
        successor.left = node.left
        successor.left.parent = successor
    del node

    return root


def rotate_right(root, node):
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
        root = y
    elif node is node.parent.left:
        node.parent.left = y
    else:
        node.parent.right = y
    y.right = node
    node.parent = y

    return root


def rotate_left(root, node):
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
        root = y
    elif node is node.parent.left:
        node.parent.left = y
    else:
        node.parent.right = y
    y.left = node
    node.parent = y

    return root


def transplant(root, u, v):
    '''
    Helper for delete(root, node) to move subtrees.
    Same algorithm from CLRS textbooks.

    :param root: root of tree
    :param u: node to move
    :param v: node to take u's place
    '''

    if root is u:
        root = v
    elif u is u.parent.left:
        u.parent.left = v
    else:
        u.parent.right = v
    if v:
        v.parent = u.parent

    return root


# Return smallest element in a tree
def tree_min(node):
    while node.left:
        node = node.left

    return node


# Create a BST with keys
def generate_bst(keys):
    tree = Node(keys[0])
    for i in keys[1:]:
        tree = insert(tree, Node(i))

    return tree


# Display elements of a tree in order
def in_order_traversal(r):
    if r:
        in_order_traversal(r.left)
        print(r.val)
        in_order_traversal(r.right)


def test_optimal_bst(p = [0, 0.15, 0.10, 0.05, 0.10, 0.20], q = [0.05, 0.10, 0.05, 0.05, 0.05, 0.10], n = 5):
    e, w, root = Optimal_BST(p, q, n)

    print('e\n', np.matrix(e), '\n')
    print('w\n', np.matrix(w), '\n')
    print('root\n', np.matrix(root))