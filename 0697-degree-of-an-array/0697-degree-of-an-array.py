class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        d = {}
        for num in nums:
            d[num] = []
        for i in range(len(nums)):
            d[nums[i]].append(i)
        lenMax = -1
        lenMin = 50001
        for key in d:
            lenMax = max(lenMax, len(d[key]))
        for key in d:
            if(len(d[key]) == lenMax):
                lenMin = min(lenMin, d[key][lenMax-1] - d[key][0] + 1)
        return lenMin