
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.


def twoSum(nums: list[int], target: int) -> list[int]:
    prevMap = {} # val: index
    
    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i
        
    return
                     
        
    
    


def main():
    nums = [2, 5, 7, 12]
    target = 9
    print(twoSum(nums, target))



if __name__ == "__main__":
    main()