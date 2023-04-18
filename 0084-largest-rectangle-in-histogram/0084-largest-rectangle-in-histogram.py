class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack=[]
        maxArea=0

        heights.append(-1)
        for i in range(len(heights)):
            index=i
            while stack and stack[-1][1]>=heights[i]:
                index,bar=stack.pop(-1)
                height=i-index
                maxArea=max(maxArea,height*bar)
            stack.append((index,heights[i]))
            
        return maxArea     
               