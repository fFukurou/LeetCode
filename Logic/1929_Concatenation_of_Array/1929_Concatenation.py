
# Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

# Specifically, ans is the concatenation of two nums arrays.

# Return the array ans.



def getConcatenation(nums : list[int]) -> list[int]:
    ans = []
    # ans = nums + nums
    for i in range(0, 2):
        for number in nums:
            ans.append(number)
    
    
    return ans





def main():
    numbers = [2, 3, 9, 12, 55]
    print(getConcatenation(numbers))


if __name__ == '__main__':
    main()