def binary_search_recursive(number, start_index, end_index):
    if start_index > end_index:
        return -1
    
    mid_index = (start_index + end_index)//2
    operation = number // mid_index
    
    if operation == mid_index:
        return mid_index
    elif operation < mid_index:
    	# print("iteration")
        return binary_search_recursive(number, start_index, mid_index - 1)
    else:
    	# print("iteration")
        return binary_search_recursive(number, mid_index + 1, end_index)

def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if type(number) is not int or number < 0:
        return None

    if number == 0 or number == 1:
    	return number

    return binary_search_recursive(number, 2, number)

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
print ("Pass" if  (10000 == sqrt(100000000)) else "Fail")
print ("Pass" if  (None == sqrt(-1)) else "Fail")
print ("Pass" if  (None == sqrt("a")) else "Fail")