"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copies = {None : None}
        result = Node(x=0)
        dummy = result
        curr = head

        while curr:
            copies[curr] = Node(x=curr.val)
            curr = curr.next

        curr = head
        while curr:
            result = copies[curr]
            result.next = copies[curr.next]
            result.random = copies[curr.random]
            result = result.next
            curr = curr.next

        return copies[head]
