# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head):
            values = set()
            current = head
            previous = ListNode(None)
            previous.next = current
            
            while current != None:
                if current.val not in values:
                    values.add(current.val) # NEEDED TO ADD THE VALUE INTO THE SET, NOT THE ENTIRE NOD LOL
                    previous = previous.next
                    current = current.next
                else:
                    previous.next = previous.next.next
                    current = current.next
            return head
        