import argparse
# other imports go here
from time \
import perf_counter as ct
import random


def get_me_random_list(n):
    """Generate list of n elements in random order
    
    :params: n: Number of elements in the list
    :returns: A list with n elements in random order
    """
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list


def sequential_search(a_list, item):
    t1 = ct()

    pos = 0
    found = False
    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos + 1

    t2 = ct()
    t = t2 - t1
    return found, t


def ordered_sequential_search(a_list, item):
    t1 = ct()

    pos = 0
    found = False
    stop = False
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos+1

    t2 = ct()
    t = t2 - t1
    return found, t


def binary_search_iterative(a_list, item):
    t1 = ct()

    first = 0
    last = len(a_list) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    t2 = ct()
    t = t2 - t1
    return found, t
    

def binary_search_recursive(a_list, item):
    t1 = ct()

    def _binary_search_recursive(a_list, item):
        if len(a_list) == 0:
            return False
        else:
            midpoint = len(a_list) // 2
            if a_list[midpoint] == item:
                return True
            else:
                if item < a_list[midpoint]:
                    return _binary_search_recursive(a_list[:midpoint], item)
                else:
                    return _binary_search_recursive(a_list[midpoint + 1:], item)

    found = _binary_search_recursive(a_list, item)
    t2 = ct()
    t = t2 - t1
    return found, t


def main():
    d = {
          'Sequential Search':         [sequential_search, 0,0,0]
        , 'Ordered Sequential Search': [ordered_sequential_search, 0,0,0]
        , 'Binary Search Iterative':   [binary_search_iterative, 0,0,0]
        , 'Binary Search Recursive':   [binary_search_recursive, 0,0,0]
    }
    e_num = 500, 1000, 5000
    n_ls = 100
    target = 99999999

    count = 0
    e = 0
    for n in e_num:
        e += 1
        for _ in range(n_ls):
            count += 1
            a_list = get_me_random_list(n)
            a_list.sort()
            for k, v in d.items():
                _, t = v[0](a_list, target)
                d[k][e] += t

    for e in range(1, e+1):
        print('%s lists of %s elements:' % (n_ls, e_num[e-1]))
        for k, v in d.items():
            print('%s took %10.7f seconds to run, on average'
                  % (k, v[e] / n_ls))
        print('')


if __name__ == "__main__":
    """Main entry point"""
    main()
