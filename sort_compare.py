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
    

def insertion_sort(a_list):
    t1 = ct()

    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index
        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1
        a_list[position] = current_value

    t2 = ct()
    t = t2 - t1
    return t


def shell_sort(a_list):
    t1 = ct()

    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)
        sublist_count //= 2

    t2 = ct()
    t = t2 - t1
    return t


def gap_insertion_sort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i
        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position -= gap
        a_list[position] = current_value


def python_sort(a_list):
    t1 = ct()

    a_list.sort()

    t2 = ct()
    t = t2 - t1
    return t


def main():
    d = {
          'Insertion Sort': [insertion_sort, 0]
        , 'Shell Sort':     [shell_sort, 0]
        , 'Python Sort':    [python_sort, 0]
    }
    count = 0
    for n in 500, 1000, 10000:
        for _ in range(100):
            count += 1
            a_list = get_me_random_list(n)
            for k, v in d.items():
                t = v[0](a_list)
                d[k][1] += t

    d.update((k, v[1] / count) for k, v in d.items())
    for k, v in d.items():
        print('%s took %10.7f seconds to run, on average' % (k, v))


if __name__ == "__main__":
    """Main entry point"""
    main()