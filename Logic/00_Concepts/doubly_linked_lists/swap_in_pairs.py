class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def print_list(self):
        output = []
        current_node = self.head
        while current_node is not None:
            output.append(str(current_node.value))
            current_node = current_node.next
        print(" <-> ".join(output))
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
        self.length += 1
        return True

    # WRITE SWAP_PAIRS METHOD HERE #
    def swap_pairs(self):
        # Step 1: Initialize a dummy node to act as a placeholder
        # for the start of the list.
        dummy_node = Node(0)
    
        # Connect this dummy node to the actual head of the list.
        # This simplifies the swapping process.
        dummy_node.next = self.head
    
        # Step 2: Initialize 'previous_node' to 'dummy_node'.
        # This helps us remember the node just before the pair
        # we are about to swap.
        previous_node = dummy_node
    
        # Step 3: Loop through the list as long as there are pairs
        # of nodes available to swap.
        while self.head and self.head.next:
    
            # Identify the first node in the pair to be swapped.
            first_node = self.head
    
            # Identify the second node in the pair to be swapped.
            second_node = self.head.next
    
            # Update 'previous_node' to point to 'second_node',
            # effectively skipping over 'first_node'.
            previous_node.next = second_node
    
            # Connect 'first_node' to the node that comes after
            # 'second_node'. This ensures we don't lose the
            # rest of the list.
            first_node.next = second_node.next
    
            # Swap 'first_node' and 'second_node' by connecting
            # 'second_node' back to 'first_node'.
            second_node.next = first_node
    
            # Update the 'prev' pointers for both 'first_node'
            # and 'second_node' to maintain the doubly-linked
            # structure.
            second_node.prev = previous_node
            first_node.prev = second_node
    
            # If there's a node after 'first_node', update its
            # 'prev' to point back to 'first_node'.
            if first_node.next:
                first_node.next.prev = first_node
    
            # Move the 'head' to the node just after 'first_node'
            # to prepare for the next iteration.
            self.head = first_node.next
    
            # Update 'previous_node' to point to 'first_node'
            # for the next pair to swap.
            previous_node = first_node
    
        # After the loop, set the new head of the list to the
        # node that comes after 'dummy_node'.
        self.head = dummy_node.next
    
        # Make sure the new head's 'prev' is set to None, as it
        # is now the first node in the list.
        if self.head:
            self.head.prev = None
                
            
        
    ################################



my_dll = DoublyLinkedList(1)
my_dll.append(2)
my_dll.append(3)
my_dll.append(4)
my_dll.append(5)
my_dll.append(6)
my_dll.append(7)

print('my_dll before swap_pairs:')
my_dll.print_list()

my_dll.swap_pairs() 


print('my_dll after swap_pairs:')
my_dll.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    my_dll before swap_pairs:
    1 <-> 2 <-> 3 <-> 4
    ------------------------
    my_dll after swap_pairs:
    2 <-> 1 <-> 4 <-> 3

"""