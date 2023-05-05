class Solution:
    def jump(self, nums: List[int]) -> int:
        length = len(nums)
        result = 0
        low = 0
        high = 0

        while high < (length-1):

            max_jump = 0

            for index in range(low,high + 1):
                max_jump = max(max_jump , index + nums[index])
            low = high + 1
            high = max_jump
            result = result + 1

        return result