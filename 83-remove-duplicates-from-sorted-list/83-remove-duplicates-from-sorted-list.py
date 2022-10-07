# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        trav = head
        
        while curr:
            if trav != None and curr.val == trav.val:
                trav = trav.next
            else:
                curr.next = trav
                curr = trav
        return head