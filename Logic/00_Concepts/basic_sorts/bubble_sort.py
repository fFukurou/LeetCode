# we go through the list, and bubble the greatest element to the end
def bubble_sort(nums):
    for i in range(len(nums) - 1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j + 1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp
    
    return nums








nums_list = [4, 2, 6, 5, 1, 3]
print(bubble_sort(nums_list))