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

    # WRITE SELECTION_SORT METHOD HERE #
# Define a method to sort a linked list in ascending order 
# using the selection sort algorithm
def selection_sort(self):
    # If the linked list has less than 2 elements, it is already sorted
    if self.length < 2:
        return
 
    # Start with the first node as the current node
    current = self.head
 
    # While there is at least one more node after the current node
    while current.next is not None:
        # Assume the current node has the smallest value so far
        smallest = current
        # Start with the next node as the inner current node
        inner_current = current.next
        
        # Find the node with the smallest value among the remaining nodes
        while inner_current is not None:
            if inner_current.value < smallest.value:
                smallest = inner_current
            inner_current = inner_current.next
        
        # If the node with the smallest value is not the current node,
        # swap their values
        if smallest != current:
            current.value, smallest.value = smallest.value, current.value        
 
        # Move to the next node
        current = current.next
        
    ####################################



my_linked_list = LinkedList(4)
my_linked_list.append(2)
my_linked_list.append(6)
my_linked_list.append(5)
my_linked_list.append(1)
my_linked_list.append(3)

print("Linked List Before Sort:")
my_linked_list.print_list()

my_linked_list.selection_sort()

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

