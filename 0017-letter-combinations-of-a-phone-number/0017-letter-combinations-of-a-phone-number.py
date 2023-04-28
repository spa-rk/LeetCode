class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_pad = self.buildNumPad()
        result = []
        
        def backtrack(self, d, curr):
            if len(d) == 0:
                if len(curr) > 0:
                    result.append("".join(curr))
                return
            letters = num_pad[d[0]]
            for i in letters:
                curr.append(i)
                backtrack(self, d[1:], curr)
                curr.pop()

        backtrack(self, digits, curr=[])
        return result
    
    def buildNumPad(self):
        num_pad = dict()
        num_pad["2"] = 'abc'
        num_pad["3"] = 'def'
        num_pad["4"] = 'ghi'
        num_pad["5"] = 'jkl'
        num_pad["6"] = 'mno'
        num_pad["7"] = 'pqrs'
        num_pad["8"] = 'tuv'
        num_pad["9"] = 'wxyz'
        return num_pad