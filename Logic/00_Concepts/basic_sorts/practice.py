
# we interate through the list, and swap the next value with the value where the index has the lowest value
# we bring the lowest value of the front
def selection_sort(nums):
    for i in range(len(nums) - 1):
        min_value_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_value_index]:
                min_value_index = j
                
        if i != min_value_index:
            temp = nums[i]
            nums[i] = nums[min_value_index]
            nums[min_value_index] = temp

    return nums





















nums_list = [4, 2, 6, 5, 1, 3]
print(selection_sort(nums_list))