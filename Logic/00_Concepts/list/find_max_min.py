# WRITE FIND_MAX_MIN FUNCTION HERE #
def find_max_min(my_list):
    if len(my_list) == 0:
        return tuple()
    
    min_value = my_list[0]
    max_value = my_list[0]
    
    for num in my_list:
        if num > max_value:
            max_value = num
        elif num < min_value:
            min_value = num
    
    return (max_value, min_value)
    
####################################
    


print( find_max_min([5, 3, 8, 1, 6, 9]) )


"""
    EXPECTED OUTPUT:
    ----------------
    (9, 1)
    
"""