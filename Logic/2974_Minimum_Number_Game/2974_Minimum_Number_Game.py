# You are given a 0-indexed integer array nums of even length and there is also an empty array arr. Alice and Bob decided to play a game where in every round Alice and Bob will do one move. The rules of the game are as follows:

# Every round, first Alice will remove the minimum element from nums, and then Bob does the same.
# Now, first Bob will append the removed element in the array arr, and then Alice does the same.
# The game continues until nums becomes empty.
# Return the resulting array arr.


def numberGame(nums: list[int]) -> list[int]:
    # length = len(nums)
    # arr = []
    
    # for i in range(int(length/2)):
    #     temp_arr = []
    #     for j in range(2):
    #         mininum = min(nums)
    #         nums.remove(mininum)
    #         temp_arr.append(mininum)

    #     arr.append(temp_arr[1])
    #     arr.append(temp_arr[0])
        

    # return arr
    nums.sort(reverse=True)
    arr= []
    i = 0
    ln = len(nums)
    while i < ln:
        a = nums.pop()
        b = nums.pop()
        arr.append(b)
        arr.append(a)
        i += 2
    # arr.reverse()
    return arr



def main():
    nums = [5,4,2,3]
    print(numberGame(nums))


if __name__ == '__main__':
    main()