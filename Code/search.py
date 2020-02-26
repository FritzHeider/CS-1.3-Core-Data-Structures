def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)

def linear_search_iterative(array, item):
    '''TODO: Time complexity: O(n)'''
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    '''TODO: Time complexity: O(n)'''
    if index >= len(array):
        return None
    if array[index] == item:
        return index
    return linear_search_recursive(array, item, index + 1)

def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return binary_search_iterative(array, item)
    return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    '''TODO: Time complexity: O(log(2)n)'''
    searching = True
    index = int(len(array) / 2)
    left = 0
    right = len(array) - 1
    while searching:
        if array[index] == item:
            return index
        elif array[index] < item:
            left = index + 1
        elif array[index] > item:
            right = index - 1
        if left > right:
            return None
        else:
            index = int((left + right) / 2)

def binary_search_recursive(array, item, left=None, right=None):
    '''TODO: Time complexity: O(log(2)n)'''
    if left is None:
        left = 0
    if right is None:
        right = len(array) - 1
    index = int((left + right) / 2)
    if left > right:
        return None
    if array[index] == item:
        return index
    elif array[index] < item:
        return binary_search_recursive(array, item, index + 1, right)
    elif array[index] > item:
        return binary_search_recursive(array, item, left, index - 1)
