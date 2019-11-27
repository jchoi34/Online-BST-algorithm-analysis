from math import inf
from Binary_Search_Tree import *

def Optimal_BST(p, n, q=None):
    '''
    Generate optimal Binary Search Tree. Indexing changed from textbook alg to accommodate lists starting at index 0.
    Uses the improvement found by Donald Knuth to make the algorithm O(n^2).
    Original O(n^3) version is also defined below.
    '''
    # e = table for building solution bottom up
    # w = store weights from previous computations; root = store subtree root choices
    e = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    w = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    root = [[0 for _ in range(n)] for _ in range(n)]

    if q is None:
        q = [0] * (n + 1)

    for i in range(n + 1):
        e[i][i] = q[i]
        w[i][i] = q[i]

    for i in range(n):
        root[i][i] = i

    for l in range(n):
        for i in range(n - l):
            j = i + l + 1
            e[i][j] = inf
            w[i][j] = w[i][j - 1] + p[j] + q[j]
            if i != j - 1:
                for r in range(root[i][j - 2], root[i + 1][j - 1] + 1):
                    t = e[i][r] + e[r + 1][j] + w[i][j]
                    if t < e[i][j]:
                        e[i][j] = t
                        root[i][j - 1] = r
            else:
                t = e[i][i] + e[i + 1][j] + w[i][j]
                e[i][j] = t

    for i in range(n):
        for j in range(i, n):
            root[i][j] += 1

    return e, w, root


# generate a BST with a table of roots
def generate_optimal_bst(roots, n):
    if n == 1:
        return Node(1)
    stack = []
    root_val = roots[0][n - 1]
    tree = Node(root_val)
    if root_val < n:
        stack.append((root_val, n - 1))
    if root_val > 1:
        stack.append((0, root_val - 2))

    while stack:
        i, j = stack.pop()
        root_val = roots[i][j]
        insert(tree, Node(root_val))
        if i == j:
            continue
        if root_val <= j:
            stack.append((root_val, j))
        if root_val - 2 >= i:
            stack.append((i, root_val - 2))

    return tree


def Optimal_BST_Original(p, q, n):
    '''
    Generate optimal Binary Search Tree. Indexing changed from textbook alg to accommodate lists starting at index 0.
    '''
    # e = table for building solution bottom up
    # w = store weights from previous computations; root = store subtree root choices
    e = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    w = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    root = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n + 1):
        e[i][i] = q[i]
        w[i][i] = q[i]

    for l in range(n):
        print(l)
        for i in range(n - l):
            j = i + l + 1
            e[i][j] = inf
            w[i][j] = w[i][j - 1] + p[j] + q[j]
            for r in range(i, j):
                t = e[i][r] + e[r + 1][j] + w[i][j]
                if t < e[i][j]:
                    e[i][j] = t
                    root[i][j - 1] = r + 1

    return e, w, root