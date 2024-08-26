
class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        for num in nums:
            if num == 0:
                nums.append(num)
                del nums[nums.index(num)]