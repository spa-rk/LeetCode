# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """
from collections import deque
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        if len(nestedList) == 0:
            return []
        self.res = []
        self.flatten(nestedList)
        
    def flatten(self, nestedList):
        for element in nestedList:
            if element.isInteger():
                self.res.append(element.getInteger())
            else:
                self.flatten(element.getList())
   
    def next(self) -> int:
        return self.res.pop(0)
    
    def hasNext(self) -> bool:
        return self.res

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())