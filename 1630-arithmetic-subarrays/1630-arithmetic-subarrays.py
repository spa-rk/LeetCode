class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res = [True]*len(l)
        for i in range(len(l)):
            new_array = sorted(nums[l[i]:r[i]+1], reverse=True)
            compare = new_array[1] - new_array[0]
            for j in range(1, len(new_array)):
                if compare != (new_array[j]-new_array[j-1]):
                    res[i] = False
                    break
        return res