# WRITE LONGEST_CONSECUTIVE_SEQUENCE FUNCTION HERE #
def longest_consecutive_sequence(nums):
    nums_set = set(nums)
    longest_sequence = 0
    
    for num in nums_set:
        if num - 1 not in nums_set:
            current_num = num
            current_sequence = 1
            
            while current_num + 1 in nums_set:
                current_num += 1
                current_sequence += 1
                
            longest_sequence = max(longest_sequence, current_sequence)
    
    return longest_sequence
    
    
    
    
    
    
####################################################



print( longest_consecutive_sequence([100, 4, 200, 1, 3, 2]) )



"""
    EXPECTED OUTPUT:
    ----------------
    4

"""