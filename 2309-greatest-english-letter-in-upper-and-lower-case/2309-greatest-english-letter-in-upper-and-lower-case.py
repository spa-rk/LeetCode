class Solution:
    def greatestLetter(self, s: str) -> str:
        l=list(ascii_lowercase)
        u=list(ascii_uppercase)
        d={}
        d1={}
        for i in s:
            if i in u and i in d:
                d[i]+=1
            elif i in u:
                d[i]=1
        for i in s:
            if i in l and i in d1:
                d1[i]+=1
            elif i in l:
                d1[i]=1
        a=[]
        for i in d:
            if i.lower() in d1:
                a.append((i,d[i]+d1[i.lower()]))
        a.sort()
        ans=''
        if len(a)!=0:
            ans+=a[-1][0]
        return ans