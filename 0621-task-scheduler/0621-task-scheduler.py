class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hmap = Counter(tasks)
        
        maxsize = max(hmap.values()) + 1
        
        bucket = [[] for i in range(maxsize)]
        
        for k,v in hmap.items():
            bucket[v].append(k)
            
        for i in range(maxsize-1,-1,-1):
            if bucket[i]:
                maxcnt = len(bucket[i])
                maxbuc = i
                break
                
        
        duration = (maxbuc - 1)*(n+1) + maxcnt
        
        return max(duration, len(tasks))