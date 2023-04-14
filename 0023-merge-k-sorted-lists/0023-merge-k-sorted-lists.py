# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        r=ListNode()
        h=[]
        heapify(h)
        for i in range(len(lists)):
            if lists[i]:
                heappush(h,(lists[i].val,i))
                lists[i]=lists[i].next
        curr=r
        while h:
            u,v=heappop(h)
            if lists[v]:
                heappush(h,(lists[v].val,v))
                lists[v]=lists[v].next
            curr.next=ListNode(u)
            curr=curr.next
        return r.next