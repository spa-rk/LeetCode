class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]

        def DFS(ind):
            if ind >= len(nums):
                return 
            now_ele = nums[ind]
            for i in range(len(ans)):
                ans.append(ans[i]+ [now_ele])
            DFS(ind+1)
        DFS(0)
        return ans