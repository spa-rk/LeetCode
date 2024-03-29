class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        unq_char = set(t)
        
        if len(s) != len(t):
            return False

        for i in unq_char:
            if t.count(i) != s.count(i):
                return False
        return True