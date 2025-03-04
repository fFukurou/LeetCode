class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    # WRITE BUBBLE_SORT METHOD HERE #
    def bubble_sort(self):
        # Check if sorting is needed. If the list has fewer
        # than 2 elements, it's already sorted. In such a
        # case, exit the function as no sorting is needed.
        if self.length < 2:
            return
        
        # Initialize 'sorted_until' to None. This marker will
        # indicate the boundary between the sorted part of
        # the list and the part that still needs sorting.
        sorted_until = None
        
        # Start the outer loop. This loop will continue
        # running until the sorted section of the list
        # includes the second node, meaning the whole
        # list is sorted.
        while sorted_until != self.head.next:
            # Initialize 'current' at the head of the list.
            # 'current' will traverse the list for sorting.
            current = self.head
    
            # Begin the inner loop. It runs until 'current'
            # reaches the 'sorted_until' node. This loop is
            # where the actual comparison and sorting happen.
            while current.next != sorted_until:
                # Identify 'next_node', the node immediately
                # following 'current'. This is essential for
                # comparing adjacent nodes.
                next_node = current.next
    
                # Compare values of 'current' and 'next_node'.
                # If 'current' is greater, swap their values.
                # This action bubbles up larger values towards
                # the end of the list, achieving sorting.
                if current.value > next_node.value:
                    current.value, next_node.value = \
                        next_node.value, current.value
                
                # Advance 'current' to the next node in the list.
                # This progression is crucial for continuing
                # the sorting process.
                current = current.next
    
            # Update 'sorted_until' after each full pass of
            # the inner loop. This moves the boundary of the
            # sorted section one node forward, shrinking the
            # unsorted section accordingly.
            sorted_until = current
        
        
    #################################



my_linked_list = LinkedList(4)
my_linked_list.append(2)
my_linked_list.append(6)
my_linked_list.append(5)
my_linked_list.append(1)
my_linked_list.append(3)

print("Linked List Before Sort:")
my_linked_list.print_list()

my_linked_list.bubble_sort()

print("\nSorted Linked List:")
my_linked_list.print_list()



"""
    EXPECTED OUTPUT:
    ----------------
    Linked List Before Sort:
    4
    2
    6
    5
    1
    3

    Sorted Linked List:
    1
    2
    3
    4
    5
    6

"""

