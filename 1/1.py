__author__ = 'Derek'


def find_best_possible_return(stock_price_array):
    if len(stock_price_array) < 2:
        return 0

    lowest_price_seen = stock_price_array[0]
    largest_delta = 0

    for i in range(len(stock_price_array)):
        if stock_price_array[i] < lowest_price_seen:
            lowest_price_seen = stock_price_array[i]
        else:
            if stock_price_array[i] - lowest_price_seen > largest_delta:
                largest_delta = stock_price_array[i] - lowest_price_seen

    return largest_delta

def main():
    #test_array = [500, 510, 600, 1005, 450, 1000, 1100, 1000, 900, 700, 400, 500]
    test_array = [1000, 900, 800, 700, 500]
    best_possible_return = find_best_possible_return(test_array)

    print best_possible_return


if __name__ == "__main__":
    main()




