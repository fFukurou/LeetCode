
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

'''plan:
1. Iterate through the array
2. For each number, iterate again to see if num1 matches num2'''


def containsDuplicate(nums: list[int]) -> bool:
    # is_duplicate: bool = False
    # nums.sort()
    # for i in range(len(nums)):
    #     if i == len(nums) - 1:
    #         pass
        
    #     elif nums[i] == nums[i+1]:
    #         is_duplicate = True
    
    # return is_duplicate
    is_duplicate: bool = False
    hashset = set()
    
    for num in nums:
        if num in hashset:
            is_duplicate = True
            
        hashset.add(num)
            
        
    return is_duplicate
    # return len(set(nums)) < len(nums)



def main():
    nums = [0, 1, 2, 3, 4, 5, 6 ,7 ,8 ,9, 10, 32]
    print(containsDuplicate(nums))
    


if __name__ == "__main__":
    main()