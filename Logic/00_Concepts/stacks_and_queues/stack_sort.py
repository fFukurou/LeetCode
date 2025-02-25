class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list.pop()




##### WRITE SORT_STACK FUNCTION HERE #####
def sort_stack(input_stack: Stack):
    # Create a new stack to hold the sorted elements
    reversed_stack = Stack()
 
    # While the original stack is not empty
    while not input_stack.is_empty():
        # Remove the top element from the original stack
        temp = input_stack.pop()
 
        # While the additional stack is not empty and 
        #the top element is greater than the current element
        while not reversed_stack.is_empty() and reversed_stack.peek() > temp:
            # Move the top element from the additional stack to the original stack
            input_stack.push(reversed_stack.pop())
 
        # Add the current element to the additional stack
        reversed_stack.push(temp)
  
    # Copy the sorted elements from the additional stack to the original stack
    while not reversed_stack.is_empty():
        input_stack.push(reversed_stack.pop())
    
##########################################




my_stack = Stack()
my_stack.push(3)
my_stack.push(1)
my_stack.push(5)
my_stack.push(4)
my_stack.push(2)


print("Stack before sort_stack():")
my_stack.print_stack()

sort_stack(my_stack)

print("\nStack after sort_stack:")
my_stack.print_stack()



"""
    EXPECTED OUTPUT:
    ----------------
    Stack before sort_stack():
    2
    4
    5
    1
    3

    Stack after sort_stack:
    1
    2
    3
    4
    5

"""