class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        p, s = list(pattern), list(s.split(" "))

        return len(s) == len(p) and len(set(zip(p, s))) == len(set(s)) == len(set(p))