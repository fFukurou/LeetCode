# WRITE THE FUNCTION HERE #
def first_non_repeating_char(string):
    # create an empty hash table to count the frequency of each character
    char_counts = {}
    # count the frequency of each character in the string
    for char in string:
        # this increments the count by 1 in the dictionary
        char_counts[char] = char_counts.get(char, 0) + 1
    # find the first non-repeating character in the string
    for char in string:
        if char_counts[char] == 1:
            return char
    # return None if no non-repeating character is found
    return None
        
    
    
###########################



print( first_non_repeating_char('leetcode') )

print( first_non_repeating_char('hello') )

print( first_non_repeating_char('aabbcc') )



"""
    EXPECTED OUTPUT:
    ----------------
    l
    h
    None

"""