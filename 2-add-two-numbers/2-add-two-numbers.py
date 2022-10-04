# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ret = ListNode(0)
        target = ret # value resulted from adding each node value from l1 and l2
        carry = 0 # When the target num becomes 2-digits
        
        while (l1 != None or l2 != None):
        # Consider a case where the length of l1 and l2 is different. 
        # So both val1 and val2 to 0 first and check if the node is not null
            val1 = 0
            val2 = 0
            
            if(l1 != None):
                val1 = l1.val
            
            if(l2 != None):
                val2 = l2.val
            
            added = val1 + val2 + carry
            carry = added // 10
            target.val = added % 10
            
            if(l1 != None):
                l1 = l1.next
            
            if(l2 != None):
                l2 = l2.next
            
            if(l1 != None or l2 != None):
                target.next = ListNode(0)
                target = target.next
                
        if (carry == 1):
            target.next = ListNode(1)
            
        return ret