# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head 

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        first = head

        if not head or not head.next:
            return

        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None

        second = self.reverse_list(second)

        while second:
            next1 = first.next
            next2 = second.next

            first.next = second
            second.next = next1

            first = next1
            second = next2

