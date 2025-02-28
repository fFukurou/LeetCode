# WRITE LONGEST_CONSECUTIVE_SEQUENCE FUNCTION HERE #
def longest_consecutive_sequence(nums): # -> O(n)
    longest_sequence = 0
    set1 = set(nums)
    
    for num in set1:
        if num - 1 not in set1:
            current_num = num
            current_sequence = 1
            
            while current_num + 1 in set1:
                current_num += 1
                current_sequence += 1
    
            longest_sequence = max(longest_sequence, current_sequence)
            
    return longest_sequence
    
    
    
    
####################################################



print( longest_consecutive_sequence([100, 4, 200, 1, 3, 2, 6, 6, 5, 7, -1, 0]) )



"""
    EXPECTED OUTPUT:
    ----------------
    4

"""