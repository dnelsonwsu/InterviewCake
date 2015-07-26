'''Write a function for doing an in-place shuffle of an array.
The shuffle must be "uniform," meaning each item in the original array must have the same probability of ending up in each spot in the final array.

Assume that you have a function get_random(floor, ceiling) for getting a random integer that is >=floor and <=ceiling.'''


import random
import pprint

def get_random(floor, ceiling):
    r = random.randint(floor, ceiling)
    return r

def randomize_array_in_place(array):
    array_size = len(array)
    for i in range(array_size - 1):
        switch_index = get_random(i, array_size - 1)
        if switch_index != i:
            tmp = array[i]
            array[i] = array[switch_index]
            array[switch_index] = tmp


def puzzle_35():
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    randomize_array_in_place(array)

    pprint.pprint(array)
    print "done"


if __name__ == "__main__":
    puzzle_35()
else:
    print "wtf"