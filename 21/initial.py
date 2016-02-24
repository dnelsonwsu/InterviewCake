from random import shuffle


# This assumes each item will appear at most twice in list
def find_unique_item(list_to_search):
    occurred_once = {}
    for item in list_to_search:
        if item in occurred_once:
            del occurred_once[item]
        else:
            occurred_once[item] = None

    return occurred_once.keys()



if __name__ == "__main__":
    drone_count = 100
    returning_drones = 99

    # Generate drones list
    drones_list = range(drone_count)
    shuffle(drones_list)

    returned_drones = drones_list[:returning_drones]

    drones_list += returned_drones
    shuffle(drones_list)

    print drones_list

    print find_unique_item(drones_list)

