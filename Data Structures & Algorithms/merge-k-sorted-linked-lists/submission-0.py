# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        dummy = ListNode(0, None)
        result = dummy
        counter = 0

        for numlist in lists:
            if numlist:
                heapq.heappush(heap, (numlist.val, counter, numlist))
                counter += 1

        while heap:
            _, _, curr = heapq.heappop(heap)
            result.next = curr
            result = result.next
            if curr.next:
                heapq.heappush(heap, (curr.next.val, counter, curr.next))
                counter += 1

        return dummy.next