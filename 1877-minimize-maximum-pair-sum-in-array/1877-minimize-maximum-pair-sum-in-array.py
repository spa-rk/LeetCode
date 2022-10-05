class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        res = []
        for i in range(len(nums)):
            res.append(nums[i] + nums[len(nums)-1-i])
            
        print(res)
        print(max(res))
        return max(res)