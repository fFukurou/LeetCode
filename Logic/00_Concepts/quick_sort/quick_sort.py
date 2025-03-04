# swaps the values of two positions in a list
def swap(my_list, index1, index2):
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp
    
    
    
# organizes every value that is less than X to the left, and every value that is greater than X to the right, then places X in the middle and returns its index
# X will generally be the first item in the list
def pivot(my_list, pivot_index, end_index):
    swap_index = pivot_index
    
    for i in range(pivot_index + 1, end_index + 1):
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1
            swap(my_list, swap_index, i)
    
    swap(my_list, pivot_index, swap_index)
    return swap_index


# recursively runs pivot(), then on the left side, then on the rigtht side
def quick_sort_helper(my_list, left, right): # ---> O(n log n ) OR O(n²) if you already have sorted data
    if left < right:
        pivot_index = pivot(my_list, left, right)
        quick_sort_helper(my_list, left, pivot_index - 1)
        quick_sort_helper(my_list, pivot_index + 1, right)
    return my_list



def quick_sort(my_list):
    return quick_sort_helper(my_list, 0, len(my_list) - 1)
    
    
    
my_list = [4, 6, 1, 7, 3, 2, 5]
print(my_list)
quick_sort(my_list)
print(my_list)