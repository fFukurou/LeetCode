# WRITE FIND_PAIRS FUNCTION HERE #
def find_pairs(arr1, arr2, target):
    # Convert arr1 to a set for O(1) lookup
    set1 = set(arr1)
    # Initialize an empty list to store the pairs
    pairs = []
    # Loop through each number in arr2
    for num in arr2:
        # Calculate the complement of the current number
        complement = target - num
        # Check if the complement is in set1
        if complement in set1:
            # If it is, add the pair to the pairs list
            pairs.append((complement, num))
    # Return the list of pairs that add up to the target value
    return pairs
    
    
    
##################################




arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 6, 8, 10]
target = 7

pairs = find_pairs(arr1, arr2, target)
print (pairs)



"""
    EXPECTED OUTPUT:
    ----------------
    [(5, 2), (3, 4), (1, 6)]

"""