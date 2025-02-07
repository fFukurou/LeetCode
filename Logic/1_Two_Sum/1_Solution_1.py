
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.


def twoSum(nums: list[int], target: int) -> list[int]:
    indexes = []
    for i in range(len(nums)):
         for j in range(len(nums)):
             if i == j: pass
             else:
                 if nums[i] + nums[j] == target:
                    indexes.append(i)
                    indexes.append(j)
                    return indexes
                     
        
    
    


def main():
    nums = [2,7,11,55]
    target = 9
    print(twoSum(nums, target))



if __name__ == "__main__":
    main()