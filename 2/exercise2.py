__author__ = 'derek'




def get_products_of_all_ints_except_at_index(list_of_ints):

    if len(list_of_ints) == 1:
        return [0]
    elif len(list_of_ints) == 0:
        return list_of_ints


    result_list = [ 1 ]
    current_multiplicand = 1

    # First pass. Starting at index 1, from left to right.
    for cur_int_index in range(1, len(list_of_ints)):
       current_multiplicand *= list_of_ints[cur_int_index - 1]
       result_list.append(current_multiplicand)

    current_multiplicand = 1
    # Second pass. Starting at last index, from right to left
    for cur_int_index in range(len(list_of_ints)-2, -1, -1):
        current_multiplicand *= list_of_ints[cur_int_index + 1]

        result_list[cur_int_index] *= current_multiplicand

    return result_list


def main():
    test_list = [1, 0, 5, 6]
    result = get_products_of_all_ints_except_at_index(test_list)
    print result


main()