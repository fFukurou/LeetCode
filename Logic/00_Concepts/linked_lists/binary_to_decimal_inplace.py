class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1
    
    def print_list(self):
        if self.head is None:
            print("empty list")
        else:
            temp = self.head
            values = []
            while temp is not None:
                values.append(str(temp.value))
                temp = temp.next
            print(" -> ".join(values)) 

    # WRITE BINARY_TO_DECIMAL METHOD HERE #
    def binary_to_decimal(self):
        current = self.head
        values = []
        
        while current != None:
            values.append(current.value)
            current = current.next
        
        
        for i in range(len(values)):
            values[len(values) - i - 1] *= (2**i)
        
        sum = 0
        for value in values:
            sum += value
            
        decimal_values = [int(digit) for digit in str(sum)]
        
        current = self.head
        for i in range(len(decimal_values)):
            current.value = decimal_values[i]
            if i != len(decimal_values) - 1:
                current = current.next
            else:
                current.next = None
            
            
        
            
        return True
            
        
        
        
    #######################################




# Test case 1: Binary number 1101 = Decimal number 13
linked_list = LinkedList(1)
linked_list.append(0)
linked_list.append(0)
linked_list.append(1)
linked_list.append(1)
linked_list.append(1)

print(" ------------ BINARY --------------")
linked_list.print_list()

linked_list.binary_to_decimal()
print(" ------------ DECIMAL --------------")
linked_list.print_list()
