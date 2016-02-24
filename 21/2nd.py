from random import shuffle


# This assumes each item will appear at most twice in list and there is only one unique item
def find_unique_id(list_to_search):
    unique_id = 0

    for item in list_to_search:
        unique_id = unique_id ^ item

    return unique_id

if __name__ == "__main__":
    drone_count = 100
    returning_drones = 99

    # Generate initial drones list
    drones_list = range(drone_count)
    shuffle(drones_list)

    # Generate a returned drones list and merge the two lists
    returned_drones = drones_list[:returning_drones]
    drones_list += returned_drones

    # One more shuffle to randomize the ordering
    shuffle(drones_list)

    print drones_list
    print find_unique_id(drones_list)

