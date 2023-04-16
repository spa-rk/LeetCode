class MinStack(object):

    def __init__(self):
        self.min = []
        self.stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if self.min and self.min[-1]>=val:
            self.min.append(val) #add temporary min values to the min stack 
        if not self.min:
            self.min.append(val) #initialization

    def pop(self):
        """
        :rtype: None
        """
        val = self.stack.pop() #pop and get value
        if self.min[-1]==val: #if it is the min value we delete it from the min stack
            self.min.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()