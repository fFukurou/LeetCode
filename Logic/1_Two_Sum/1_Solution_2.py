
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.


def twoSum(nums: list[int], target: int) -> list[int]:
    indexes = []
    for i in range(len(nums)):
        difference = target - nums[i]
        nums2 = nums.copy()
        nums2[i] = None
        
        if difference in nums2:
            return [i, nums2.index(difference)]
                     
        
    
    


def main():
    nums = [0,4,3,0]
    target = 0
    print(twoSum(nums, target))



if __name__ == "__main__":
    main()