class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        output = []

        def subset(idx):
            if len(nums) <= idx:
                return
            output.append(nums[idx])
            res.append(output[:])
            subset(idx+1)
            output.pop()
            subset(idx+1)

        subset(0)
        return res  