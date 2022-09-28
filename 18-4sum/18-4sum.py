class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return
        dic = {}
        res = []
        nums.sort()
        
        for i in reversed(range(3, len(nums))):
            if i == len(nums) - 1 or nums[i] != nums[i + 1]:
                for j in reversed(range(2, i)):
                    if j == i - 1 or nums[j] != nums[j + 1]:
                        sum2 = nums[i] + nums[j]
                        dic[sum2] = dic.get(sum2, []) + [[j, i]]

        for i in range(len(nums) - 3):
            if i == 0 or nums[i - 1] != nums[i]:
                for j in range(i + 1, len(nums) - 2):
                    if j == i + 1 or nums[j - 1] != nums[j]:
                        if target - nums[i] - nums[j] in dic:
                            for x in dic[target - nums[i] - nums[j]]:
                                if j < x[0]:
                                    res.append([nums[i], nums[j], nums[x[0]], nums[x[1]]])
        return res