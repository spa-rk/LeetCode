class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def generator(prefix, left, right):
            if left:
                generator(prefix + '(', left-1, right)
            if left < right:
                generator(prefix + ')', left, right-1)
            if right == 0:
                ans.append(prefix)
            return ans
        return generator('', n, n)