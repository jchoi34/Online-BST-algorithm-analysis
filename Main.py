from Optimal_BST import *
from Key_Distribution_Generator import *
import Splay_Tree as st
import Singe_Rotation_Tree as srt
import Dynamic_Monotone_Tree as dmt
import Binary_Search_Tree as bst
import random
import sys

'''
TODO: Make each specific tree its own class extending the BST super class and override insert method.
Also, would be good to make the Node class its own seperate class while each 
tree class just holds a root pointer property.
The test functions below could then be merged into just one test function.
Also, it probably makes more sense from a design perspective as what should probably be tree class methods 
should not be function calls. It would also probably reduce the number of root variable reassignments 
throughout the entire program.
'''

'''REMOVE THIS IMPORT LATER!!!'''
import numpy as np
'''REMOVE THIS IMPORT LATER!!!'''


# Compute optimal BST
def optimal_bst_tables(key_access_dist):
    return Optimal_BST(key_access_dist, num_elems) # parameters: p, n


'''Tree generation functions'''
# Generator for bst
def gen_bst(elems):
    return bst.generate_bst(elems)


# Generator for splay tree
def gen_splay_tree(elems):
    return st.generate_splay_tree(elems)


# Generator for tree using single-rotate heuristic
def gen_srt(elems):
    return srt.generate_srt(elems)


# Generator for Dynamic monotone tree
def gen_dmt(elems, sum_list, key_access_dist):
    return dmt.generate_dmt_tree([key for key, _ in key_access_dist])


'''
Tree testing functions
TODO: Could merge all of these into one if each tree was a subclass class of Binary_Search_Tree 
with an overwritten method for search.
'''
# testing for bst
def test_bst(elems, sum_list, bst_tree):
    access_frequencies = dict.fromkeys(elems, 1)
    max_val = sum_list[len(elems) - 1]
    cost = 0
    for i in range(num_accesses):
        rand_val = random.randrange(1, max_val + 1)
        index = binary_search_sum_list(sum_list, 0, num_elems, rand_val)
        bst_tree, _, search_cost = bst.search(bst_tree, elems[index])
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
        splay_tree, search_cost = st.splay_search(splay_tree, elems[index])
        access_frequencies[elems[index]] += 1
        cost += search_cost

    return [0] + [freq for _, freq in convert_freq_dict_to_sorted_freq_list(access_frequencies)], splay_tree, cost


# testing for tree using single-rotate heuristic
def test_srt(elems, sum_list, srt_tree):
    access_frequencies = dict.fromkeys(elems, 1)
    max_val = sum_list[len(elems) - 1]
    cost = 0
    for i in range(num_accesses):
        rand_val = random.randrange(1, max_val + 1)
        index = binary_search_sum_list(sum_list, 0, num_elems, rand_val)
        srt_tree, search_cost = srt.srt_search(srt_tree, elems[index])
        access_frequencies[elems[index]] += 1
        cost += search_cost

    return [0] + [freq for _, freq in convert_freq_dict_to_sorted_freq_list(access_frequencies)], srt_tree, cost


# testing for Dynamic monotone tree
def test_dmt(elems, sum_list, dmt_tree):
    access_frequencies = dict.fromkeys(elems, 1)
    max_val = sum_list[len(elems) - 1]
    cost = 0
    for i in range(num_accesses):
        rand_val = random.randrange(1, max_val + 1)
        index = binary_search_sum_list(sum_list, 0, num_elems, rand_val)
        dmt_tree, search_cost = dmt.dmt_search(dmt_tree, elems[index])
        access_frequencies[elems[index]] += 1
        cost += search_cost

    return [0] + [freq for _, freq in convert_freq_dict_to_sorted_freq_list(access_frequencies)], dmt_tree, cost


# cost of static bst
def cost_static_bst(tree, frequencies):
    if tree is none or frequencies is none:
        return -1

    cost = 0
    key = 1
    for freq in frequencies:
        depth = bst.depth(tree, key)
        cost += (1 + depth) * freq

    return cost


def main():
    # sys.setrecursionlimit(1500)  # Change this to print trees with very long paths
    random.seed(5)
    random_elems = gen_random_list(num_elems)  # <num_elems> random elements from 1 to <num_elems>
    '''
    Generate list of <num_elements> random elements from 1 to <elem_range>
    Then use the list from the first step to create a list where the 
    element at index i, for 1 <= i <= num_elements, is the sum of the first i elements
    '''
    sum_list = gen_sum_list(gen_random_list(num_elems, elem_range))
    key_access_dist = gen_sorted_freq_list(random_elems, num_elems, elem_range, num_accesses, sum_list)

    # generate trees
    dmt_tree = gen_dmt(random_elems, sum_list, key_access_dist)
    srt_tree = gen_bst(random_elems)
    splay_tree = gen_bst(random_elems)

    '''test each tree with <num_accesses> searches for random keys'''
    random.seed(5)
    splay_access_freq, splay_tree, cost = test_splay_tree(random_elems, sum_list, splay_tree)
    print(cost)
    random.seed(5)
    srt_access_freq, srt_tree, cost = test_srt(random_elems, sum_list, srt_tree)
    print(cost)
    random.seed(5)
    dmt_access_freq, dmt_tree, cost  = test_dmt(random_elems, sum_list, dmt_tree)
    print(cost)

    e, w, r = optimal_bst_tables(splay_access_freq)
    tree = generate_optimal_bst(r, num_elems)
    print(splay_access_freq)

num_elems = 1000
num_accesses = 10000
elem_range = 100
main()