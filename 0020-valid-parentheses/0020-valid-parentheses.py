class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        right = set([')', ']', '}'])
        dic = {'(': ')', '[': ']', '{': '}'}
        for c in s:
            if len(stack) == 0:
                stack.append(c)
            elif dic.get(stack[len(stack) - 1]) == c:
                stack.pop()
            elif c in right:
                return False
            else:
                stack.append(c)

        if len(stack) == 0:
            return True
        else:
            return False