import random
import collections

# Swap two element in a list
def swap(elems, pos1, pos2):
    elems[pos1], elems[pos2] = elems[pos2], elems[pos1]


# Generate a randomized list
def gen_random_list(num_elems, elem_range = 0):
    if elem_range == 0:
        rand_list = [i for i in range(1, num_elems + 1)]
    else:
        rand_list = [random.randrange(1, elem_range + 1) for _ in range(1, num_elems + 1)]
        return rand_list

    for i in range(num_elems):
        swap(rand_list, i, random.randrange(i, num_elems))

    return rand_list


# Generate a list where each element is the sum of the element at index i and all elements before it the list arg
def gen_sum_list(elems):
    sum_list = [elems[0]]
    for i in range(1, len(elems)):
        sum_list.append(sum_list[i - 1] + elems[i])

    return sum_list


# Search for index of x in a list such that elems[mid - 1] < x <= elems[mid]
def binary_search_sum_list(elems, l, r, x):
    while l <= r:
        mid = l + (r - l) // 2

        if elems[mid] == x:
            return mid
        elif elems[mid] < x:
            l = mid + 1
        else:
            r = mid - 1

    return l


# Generate the non-uniform access distribution of keys in a tree
def gen_key_access_dist(elems, num_elems, elem_range, num_accesses, sum_list=None):
    access_frequencies = dict.fromkeys(elems, 1)
    if not sum_list:
        sum_list = gen_sum_list(gen_random_list(num_elems, elem_range))
    max_val = sum_list[num_elems - 1]

    for i in range(num_accesses):
        rand_val = random.randrange(1, max_val + 1)
        index = binary_search_sum_list(sum_list, 0, num_elems, rand_val)
        access_frequencies[elems[index]] += 1

    return access_frequencies


def compute_frequencies(key_access_dist):
    counter = collections.Counter(key_access_dist)
    sum_accesses = sum(counter.values())
    for key in key_access_dist.keys():
        key_access_dist[key] = key_access_dist[key] / sum_accesses

    return key_access_dist


def convert_freq_dict_to_sorted_freq_list(key_access_dist):
    freq_list = [(key, value) for key, value in key_access_dist.items()]
    freq_list.sort(key=lambda tuple: tuple[1], reverse=True)

    return freq_list


def gen_sorted_freq_list(elems, num_elems, elem_range, num_accesses, sum_list):
    key_access_dist = gen_key_access_dist(elems, num_elems, elem_range, num_accesses, sum_list)
    # key_access_dist = compute_frequencies(key_access_dist)
    key_access_dist = convert_freq_dict_to_sorted_freq_list(key_access_dist)

    return key_access_dist


# Generate a random non-uniform access distribution of keys in a tree
def random_key_access_dist(num_elems, elem_range, num_accesses = 10000):
    return gen_key_access_dist(gen_random_list(num_elems), num_elems, elem_range, num_accesses)