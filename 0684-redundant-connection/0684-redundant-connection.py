class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)
        parent=[-1]*(n+1)
        rank=[0]*(n+1)
        t=[]
        def find(a):
            if parent[a]==-1:
                return a
            parent[a]=find(parent[a])
            return parent[a]
        def union(From,To):
            a=find(From)
            b=find(To)
            if a==b:
                t.append(From)
                t.append(To)
            else:
                if rank[a]>rank[b]:
                    parent[b]=a
                elif rank[b]>rank[a]:
                    parent[a]=b
                else:
                    parent[a]=b
                    rank[b]+=1
        for i in range(n):
            union(edges[i][0],edges[i][1])
            if len(t)!=0:
                return t