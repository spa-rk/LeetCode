class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1 = nums1+nums2 
        nums1.sort()
        size = len(nums1)
        if size % 2 == 0:
            median = (nums1[int(size/2)-1] + nums1[int(size/2)]) / 2
        else:
            median = nums1[int(size/2)]
        return median