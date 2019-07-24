def find_pivot_recursive(input_list, target, start_index, end_index):
    if start_index > end_index:
        return -1
    
    mid_index = (start_index + end_index)//2
    mid_element = input_list[mid_index]
    
    if mid_element < input_list[mid_index-1]:
        return mid_index
    elif target < mid_element:
        return find_pivot_recursive(input_list, target, mid_index + 1, end_index)
    else:
        return find_pivot_recursive(input_list, target, start_index, mid_index - 1)

def binary_search_recursive(array, target, start_index, end_index):
    if start_index > end_index:
        return -1
    
    mid_index = (start_index + end_index)//2
    mid_element = array[mid_index]
    
    if mid_element == target:
        return mid_index
    elif target < mid_element:
        return binary_search_recursive(array, target, start_index, mid_index - 1)
    else:
        return binary_search_recursive(array, target, mid_index + 1, end_index)

def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    # find the pivot
    pivot = None
    pivot_number = input_list[0]

    pivot = find_pivot_recursive(input_list, pivot_number, 0, len(input_list)-1)

    # if pivot equal to -1 it could be already sorted list (no rotation) or one element only
    if pivot == -1 and input_list[0] < input_list[pivot]:
        pivot = 0
    # pivot is the target element and 
    elif pivot == -1 and input_list[0] > input_list[pivot]:
        pivot = 1
    
    input_list = input_list[pivot:] + input_list[0:pivot]
    
    # find element
    result = binary_search_recursive(input_list, number, 0, len(input_list)-1)

    if result == -1:
        return result

    return (result + pivot) % len(input_list)

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[26, 27, 1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25], 27])
test_function([[26, 1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25], 26])
test_function([[1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25], 1])