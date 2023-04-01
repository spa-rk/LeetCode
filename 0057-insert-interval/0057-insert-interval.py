class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res=[]
        if len(intervals)==0:
            return [newInterval]
        for i in range(len(intervals)):
            if intervals[i][0]>newInterval[1]:
                res.append(newInterval)
                res+=intervals[i:]
                return res
            elif intervals[i][1]<newInterval[0]:
                res.append(intervals[i])
            else:
                newInterval[0]=min(intervals[i][0],newInterval[0])
                newInterval[1]=max(intervals[i][1],newInterval[1])
        res.append(newInterval)
        return res
        
        