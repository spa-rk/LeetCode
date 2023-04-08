class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ''
        for i in s:
            if i.isalpha() or i.isdigit():
                res += i.lower()
        return res == res[::-1]