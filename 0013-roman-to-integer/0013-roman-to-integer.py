class Solution:
    def romanToInt(self, s: str) -> int:
        conv = {'I': 1, 'V': 5, 'X':10, 'L':50, 'C':100, 'D': 500, 'M':1000}
        arr = []
        initial = 0
        ans = 0
        for i in s:
            if conv[i] > initial:
                ans = ans - initial
            else:
                ans = ans + initial
            initial = conv[i]
            
        return ans + initial