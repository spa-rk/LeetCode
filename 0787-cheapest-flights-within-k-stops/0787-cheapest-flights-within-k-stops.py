class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        
        for flight in flights:
            adj[flight[0]].append((flight[1], flight[2]))
            
        stops = [math.inf] * n
        
        h = []
        
        heapq.heappush(h, (0, 0, src))
        
        while h:
            temp = heapq.heappop(h)
            dist = temp[0]
            steps = temp[1]
            node = temp[2]
            
            if (steps > stops[node] or steps > k + 1):
                continue
            
            stops[node] = steps
            
            if node == dst:
                return dist
            
            if node not in adj:
                continue
            
            for neighbour in adj[node]:
                heapq.heappush(h, (dist + neighbour[1],  steps + 1, neighbour[0]))
                              
        return -1