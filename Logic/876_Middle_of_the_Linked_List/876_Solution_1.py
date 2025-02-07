# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Given the head of a singly linked list, return the middle node of the linked list.

# If there are two middle nodes, return the second middle node.


def middleNode(head):
    slow = head
    fast = head
    
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        
    return slow


def main():
    head = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5, ListNode(6))))))
    print(middleNode(head).val)


if __name__ == "__main__":
    main()