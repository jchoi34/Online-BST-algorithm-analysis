from Optimal_BST import *
from Key_Distribution_Generator import *
from Node import *
from math import inf
from Splay_Tree import *
from Singe_Rotation_Tree import *
from Dynamic_Monotone_Tree import *
from Binary_Search_Tree import *
import random
import sys

# Compute optimal BST
def optimal_bst_tables(key_access_dist):
    return Optimal_BST(key_access_dist, num_elems) # parameters: p, n


'''
Tree testing functions
TODO: Could merge all of these into one if each tree overrides search in BinarySearchTree class.
'''
# testing for bst
def test_bst(elems, sum_list, bst_tree):
    access_frequencies = dict.fromkeys(elems, 1)
    max_val = sum_list[len(elems) - 1]
    cost = 0
    for i in range(num_accesses):
        rand_val = random.randrange(1, max_val + 1)
        index = binary_search_sum_list(sum_list, 0, num_elems, rand_val)
        _, _, search_cost = bst_tree.search(elems[index])
        access_frequencies[elems[index]] += 1
        cost += search_cost

    return [0] + [freq for _, freq in convert_freq_dict_to_sorted_freq_list(access_frequencies)], cost


# testing for splay tree
def test_splay_tree(elems, sum_list, splay_tree):
    access_frequencies = dict.fromkeys(elems, 1)
    max_val = sum_list[len(elems) - 1]
    cost = 0
    for i in range(num_accesses):
        rand_val = random.randrange(1, max_val + 1)
        index = binary_search_sum_list(sum_list, 0, num_elems, rand_val)
        search_cost = splay_tree.splay_search(elems[index])
        access_frequencies[elems[index]] += 1
        cost += search_cost

    return [0] + [freq for _, freq in convert_freq_dict_to_sorted_freq_list(access_frequencies)], cost


# testing for tree using single-rotate heuristic
def test_srt(elems, sum_list, srt_tree):
    access_frequencies = dict.fromkeys(elems, 1)
    max_val = sum_list[len(elems) - 1]
    cost = 0
    for i in range(num_accesses):
        rand_val = random.randrange(1, max_val + 1)
        index = binary_search_sum_list(sum_list, 0, num_elems, rand_val)
        search_cost = srt_tree.srt_search(elems[index])
        access_frequencies[elems[index]] += 1
        cost += search_cost

    return [0] + [freq for _, freq in convert_freq_dict_to_sorted_freq_list(access_frequencies)], cost


# testing for Dynamic monotone tree
def test_dmt(elems, sum_list, dmt_tree):
    access_frequencies = dict.fromkeys(elems, 1)
    max_val = sum_list[len(elems) - 1]
    cost = 0
    for i in range(num_accesses):
        rand_val = random.randrange(1, max_val + 1)
        index = binary_search_sum_list(sum_list, 0, num_elems, rand_val)
        search_cost = dmt_tree.dmt_search(elems[index])
        access_frequencies[elems[index]] += 1
        cost += search_cost

    return [0] + [freq for _, freq in convert_freq_dict_to_sorted_freq_list(access_frequencies)], cost


# cost of static bst
def cost_static_bst(tree, frequencies):
    if tree is None or frequencies is None:
        return -1

    cost = 0
    key = 1
    for freq in frequencies:
        depth = tree.depth(key)
        cost += (1 + depth) * freq
        key += 1

    return cost


def main():
    # sys.setrecursionlimit(1500)  # Change this to print trees with very long paths using <tree>.display()
    num_tests = 10
    '''test each tree with <num_accesses> searches for random keys'''

    # splay tree tests
    random.seed(5)
    average_online_cost = 0
    min_static_cost = inf
    for _ in range(num_tests):
        random_elems = gen_random_list(num_elems)
        splay_tree = SplayTree()
        splay_tree.generate_bst(random_elems)
        # splay_tree = st.generate_splay_tree(random_elems)
        sum_list = gen_sum_list(gen_random_list(num_elems, elem_range))
        tree_access_freq, cost = test_splay_tree(random_elems, sum_list, splay_tree)
        e, w, r = optimal_bst_tables(tree_access_freq)
        tree = generate_optimal_bst(r, num_elems)
        static_cost = cost_static_bst(tree, tree_access_freq)
        average_online_cost += cost
        if static_cost < min_static_cost:
            min_static_cost = static_cost
        # print('Splay tree')
        # print('Online cost:', cost)
        # print('Static cost:', static_cost)
    print('Splay tree averages')
    print('Average online cost:', average_online_cost / num_tests)
    print('Minimum static cost:', min_static_cost)

    # single rotate tree tests
    average_online_cost = 0
    min_static_cost = inf
    for _ in range(num_tests):
        random_elems = gen_random_list(num_elems)
        srt_tree = SingleRotateTree()
        srt_tree.generate_bst(random_elems)
        # srt_tree = srt.generate_srt(random_elems)
        sum_list = gen_sum_list(gen_random_list(num_elems, elem_range))
        tree_access_freq, cost = test_srt(random_elems, sum_list, srt_tree)
        e, w, r = optimal_bst_tables(tree_access_freq)
        tree = generate_optimal_bst(r, num_elems)
        static_cost = cost_static_bst(tree, tree_access_freq)
        average_online_cost += cost
        if static_cost < min_static_cost:
            min_static_cost = static_cost
        # print('Single-rotate tree')
        # print('Online cost:', cost)
        # print('Static cost:', static_cost)
    print('Single-rotate tree averages')
    print('Average online cost:', average_online_cost / num_tests)
    print('Minimum static cost:', min_static_cost)

    # dynamic monotone tree tests
    average_online_cost = 0
    min_static_cost = inf
    for _ in range(num_tests):
        random_elems = gen_random_list(num_elems)
        sum_list = gen_sum_list(gen_random_list(num_elems, elem_range))
        key_access_dist = gen_sorted_freq_list(random_elems, num_elems, elem_range, num_accesses, sum_list)
        dmt_tree = DynamicMonotoneTree()
        dmt_tree.generate_dmt_tree([key for key, _ in key_access_dist])
        tree_access_freq, cost = test_dmt(random_elems, sum_list, dmt_tree)
        e, w, r = optimal_bst_tables(tree_access_freq)
        tree = generate_optimal_bst(r, num_elems)
        static_cost = cost_static_bst(tree, tree_access_freq)
        average_online_cost += cost
        if static_cost < min_static_cost:
            min_static_cost = static_cost
        # print('Dynamic monotone tree')
        # print('Online cost:', cost)
        # print('Static cost:', static_cost)
    print('Dynamic monotone tree averages')
    print('Average online cost:', average_online_cost / num_tests)
    print('Minimum static cost:', min_static_cost)

num_elems = 1000
num_accesses = 10000
elem_range = 100
main()