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
    
    
    def append(self, value) -> bool: # at the end of the linked list
        new_node = Node(value)
        
        if self.head == None: # if list is empty
            self.head = new_node
            self.tail = new_node
        else: # if list is not empty
            self.tail.next = new_node
            self.tail = new_node
            
        self.length += 1
        return True
    
    
    def pop(self) -> Node: # remove item from the end of a list
        if self.length == 0:
            return None
           
        temp = self.head
        pre = self.head
        
        while temp.next != None:
            pre = temp
            temp = temp.next
    
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        
        if self.length == 0: # checking if length is 0 after decrementing length by 1, which solves the edge case of only having one Node in the linked list
            self.head = None
            self.tail = None
        
        return temp
            
            
    def prepend(self, value) -> bool: # add item at the beginning of a list
        new_node = Node(value)
        
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        
        else:
            new_node.next = self.head
            self.head = new_node    
        
        self.length += 1
        return True
            
        
    def pop_first(self) -> Node:
        if self.length == 0:
            return None
        
        if self.length == 1:
            self.tail = None
        
        temp = self.head
        self.head = self.head.next
        temp.next = None
        
        self.length -= 1
        return temp
    
    
    def get(self, index) -> Node:
        if index < 0 or index >= self.length:
            return None
        
        temp = self.head
        
        # if index == 0: --------> Not necessary because of how range() works in python... if it is (0,0) then it doesn't execute at all
        #     return temp
        
        for _ in range(index):
            temp = temp.next
        
        return temp
    

    def set_value(self, index, value) -> bool:
        temp = self.get(index)
        if temp is not None:
            temp.value = value
            return True
        return False
            
        
    def insert(self, index, value) -> bool: # insert a value into an index
        if index < 0 or index > self.length:
            return False
        
        if index == 0:
            return self.prepend(value)
        
        if index == self.length:
            return self.append(value)
        
        new_node = Node(value)
        temp = self.get(index - 1)
        
        new_node.next = temp.next
        temp.next = new_node
          
        self.length += 1
        return True
        
        
    def remove(self, index) -> Node:
        if index < 0 or index >= self.length:
            return None
        
        if index == 0:
            return self.pop_first()
            
        if index == self.length - 1:
            return self.pop()
        
        prev = self.get(index - 1)
        temp = prev.next
        
        prev.next = temp.next
        temp.next = None
        
        self.length -= 1
        return temp
        
    
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        
        before = None
        after = temp.next
        
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
    
        
my_linked_list = LinkedList(4)

my_linked_list.append(7)
my_linked_list.append(13)
# print("Node of value:", my_linked_list.pop().value,  "was removed!")
my_linked_list.prepend(99)
# my_linked_list.pop_first()
# my_linked_list.pop_first()
# my_linked_list.pop_first()

my_linked_list.set_value(1, 15)

my_linked_list.insert(3, 66)
my_linked_list.remove(1)

print(my_linked_list.print_list())
# print(my_linked_list.get(2))
my_linked_list.reverse()
print(" ------------ REVERSED LIST --------------")
print(my_linked_list.print_list())


















