class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums: return [-1, -1]
        
        start, end = -1, -1
        left, right = 0, len(nums)
        res = []
   
        # binary search right
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid
            else:
                left = mid + 1
        if nums[right-1] == target:
            end = right - 1    

        # binary search left
        left, right = 0, len(nums)    
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        if left < len(nums) and nums[left] == target:
            start = left 
            
        res.append(start)
        res.append(end)
        
        return res
                

        
        