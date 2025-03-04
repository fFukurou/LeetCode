# we compare a item to the previous item, and INSERT it into that spot, moving nodes forward
def insertion_sort(nums):
    for i in range(1, len(nums)):
        temp = nums[i]
        j = i - 1
        while temp < nums[j] and j > -1:
            nums[j+1] = nums[j]
            nums[j] = temp
            j -= 1
    
    return nums





nums_list = [4, 2, 6, 5, 1, 3]
print(insertion_sort(nums_list))