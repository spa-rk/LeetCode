def merge(l,r):
    if len(l)==0 and len(r)==0:
        return []
    elif len(l)==0 or len(r)==0:
        return l+r
    res=[]
    while l or r:
        if l[0]<=r[0]:
            res.append(l.pop(0))
        else:
            res.append(r.pop(0))
        if len(l)==0 or len(r)==0:
            res+=l+r
            break
    return res

def mergeSort(nums):
    if len(nums)>1:
        m = int(len(nums)/2)
        l = mergeSort(nums[:m])
        r = mergeSort(nums[m:])
        # print("going to merge",l,r)
        return merge(l,r)
    return nums

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums)==0 or len(nums)==1:
            return nums
        return mergeSort(nums)