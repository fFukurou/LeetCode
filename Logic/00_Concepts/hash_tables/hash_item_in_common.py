def item_in_common(list1, list2):
    # create an empty dictionary to store list1's values
    my_dict = {}
 
    # iterate through list1 and add each value to the dictionary as a key
    for i in list1:
        my_dict[i] = True
 
    # iterate through list2 and check if each value is a key in the dictionary
    for j in list2:
        # if a value in list2 is also in the dictionary, return True
        if j in my_dict:
            return True
 
    # if no values in common are found, return False
    return False
        
    
    
######################################




list1 = [1,3,5]
list2 = [2,4,5]


print(item_in_common(list1, list2))



"""
    EXPECTED OUTPUT:
    ----------------
    True

"""