def binary_search(my_item, my_sorted_list):
    '''
    function that uses the binary search algorithm
    to find whether my_item is in my_list,
    and if so, in which position.
    returns: 
        (True, listindex) if item is in list;
        (False, None) otherwise
    '''

    # define the initial search limits
    lower_limit = 0
    upper_limit = len(my_sorted_list) - 1

    # while we still have a list with more than 1 number to search:
    while lower_limit <= upper_limit:
    
        middle_index = (lower_limit + upper_limit) // 2

        if my_sorted_list[middle_index] == my_item: # if we found the item,
            return True, middle_index
        elif my_sorted_list[middle_index] < my_item: # if item is SMALLERTHAN,
            lower_limit = middle_index + 1 # change lower limit
        elif my_sorted_list[middle_index] > my_item: # if item is LARGERTHAN,
            upper_limit = middle_index - 1 # change upper limit
        else:
            raise ValueError("This should not be happening")

    return False, None