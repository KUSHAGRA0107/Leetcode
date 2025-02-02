class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for i in range(len(nums) - 1):
            value = nums[i] + nums[i + 1]
            if value % 2 == 0:
                return False
        return True