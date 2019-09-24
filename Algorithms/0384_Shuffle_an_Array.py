import random

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.length = len(nums)

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums
        

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        rs = self.nums.copy()
        for i in range(self.length):
            tmp = random.randint(i, self.length - 1)
            rs[i], rs[tmp] = rs[tmp], rs[i]
        
        return rs


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
