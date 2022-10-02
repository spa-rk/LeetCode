class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        t = 0
        maj = nums[0]
        for x in nums:
            if x == maj:
                t += 1
            elif t == 0:
                maj = x
                t = 1
            else:
                t -= 1
        return maj