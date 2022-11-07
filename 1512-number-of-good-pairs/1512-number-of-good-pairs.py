class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        k = {}
        count = 0
        
        for i in nums:
            if i in k:
                count += k[i]
                k[i] += 1
            else:
                k[i] = 1
            
        return count        