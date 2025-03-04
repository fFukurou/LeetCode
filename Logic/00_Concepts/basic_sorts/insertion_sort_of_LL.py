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

    # WRITE INSERTION_SORT METHOD HERE #
    def insertion_sort(self):
        # Check if the length of the list is less than 2
        if self.length < 2:
            return
        
        # Set the pointer to the first element of the sorted list
        sorted_list_head = self.head
        
        # Set the pointer to the second element of the list
        unsorted_list_head = self.head.next
        
        # Remove the first element from the sorted list
        sorted_list_head.next = None
        
        # Iterate through the unsorted list
        while unsorted_list_head is not None:
            # Save the current element
            current = unsorted_list_head
            
            # Move the pointer to the next element in the unsorted list
            unsorted_list_head = unsorted_list_head.next
            
            # Insert the current element into the sorted list
            if current.value < sorted_list_head.value:
                # If the current element is smaller than the first element 
                # in the sorted list, it becomes the new first element
                current.next = sorted_list_head
                sorted_list_head = current
            else:
                # Otherwise, search for the appropriate position to insert the current element
                search_pointer = sorted_list_head
                while search_pointer.next is not None and current.value > search_pointer.next.value:
                    search_pointer = search_pointer.next
                current.next = search_pointer.next
                search_pointer.next = current
        
        # Update the head and tail of the list
        self.head = sorted_list_head
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        self.tail = temp
    ####################################





my_linked_list = LinkedList(4)
my_linked_list.append(2)
my_linked_list.append(6)
my_linked_list.append(5)
my_linked_list.append(1)
my_linked_list.append(3)

print("Linked List Before Sort:")
my_linked_list.print_list()

my_linked_list.insertion_sort()

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

