# takes two SORTED LISTS and merge them together
def merge(list1, list2):
    combined = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1
    
    while i < len(list1):
        combined.append(list1[i])
        i += 1
            
    while j < len(list2):
        combined.append(list2[j])
        j += 1
    return combined
    
# will break lists in half, so we can put them bcck together with the 'merge' helper function
def merge_sort(my_list): # ---> O(n log n )
    if len(my_list) == 1:
        return my_list
    mid_index = int(len(my_list)/2)
    left = merge_sort(my_list[:mid_index])
    right = merge_sort(my_list[mid_index:])
    
    return merge(left, right)
    
    
    
my_list = [3, 1, 4, 2, 7, 6, 8]

print(merge_sort(my_list))