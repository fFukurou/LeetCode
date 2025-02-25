# WRITE FIND_DUPLICATES FUNCTION HERE #
def find_duplicates(nums):
    # Create an empty dictionary named 'num_counts'.
    # This will be used to keep track of the frequency of each number
    # in the 'nums' list.
    num_counts = {}
 
    # Start a loop that iterates over each number in the 'nums' list.
    for num in nums:
        # For the current number 'num', update its count in the 'num_counts'
        # dictionary. If 'num' is not already in the dictionary, get(num, 0)
        # will return 0. Then, 1 is added to this value, effectively
        # initializing the count to 1 the first time 'num' is encountered.
        # If 'num' is already in the dictionary, its count is incremented by 1.
        num_counts[num] = num_counts.get(num, 0) + 1
    # Initialize an empty list called 'duplicates'.
    # This list will store all the numbers that appear more than once in 'nums'.
    duplicates = []
 
    # Iterate over each key-value pair in the 'num_counts' dictionary.
    # 'num' is the number from the list, and 'count' is its frequency.
    for num, count in num_counts.items():
        # Check if the count of the current number is greater than 1.
        # A count greater than 1 indicates that the number is a duplicate.
        if count > 1:
            # If the current number is a duplicate, append it to the
            # 'duplicates' list.
            duplicates.append(num)
 
    # After the loop, return the 'duplicates' list, which now contains
    # all numbers that were found more than once in the input list 'nums'.
    return duplicates
    
    
        
    
    
#######################################




print ( find_duplicates([1, 2, 3, 4, 5]) )
print ( find_duplicates([1, 1, 2, 2, 3]) )
print ( find_duplicates([1, 1, 1, 1, 1]) )
print ( find_duplicates([1, 2, 3, 3, 3, 4, 4, 5]) )
print ( find_duplicates([1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ( find_duplicates([1, 1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ( find_duplicates([]) )



"""
    EXPECTED OUTPUT:
    ----------------
    []
    [1, 2]
    [1]
    [3, 4]
    [1, 2, 3]
    [1, 2, 3]
    []

"""

