class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dic = {}
        def recursive(i,total):
            if i == len(nums):
                return 1 if total == target else 0
            if (i,total) in dic:
                return dic[(i,total)]
            dic[(i,total)] = (recursive(i+1,total+nums[i])+recursive(i+1,total-nums[i]))
            return dic[(i,total)]
        return recursive(0,0)