class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if len(nums1) == 0 and len(nums2) == 0:
            return []
        if len(nums1) == 0:
            return nums2
        if len(nums2) == 0:
            return nums1
        
        for i in nums2:
            nums1.append(i)
            nums1.remove(0)
            
        if len(nums1) == m+n:
            nums1.sort()
        