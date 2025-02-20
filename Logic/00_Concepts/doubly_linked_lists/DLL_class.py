class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
        
    def print_list(self) -> None:
        temp = self.head
        
        while temp is not None:
            print(temp.value)
            temp = temp.next

    
    def append(self, value) -> bool:
        new_node = Node(value)
        
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        
        self.length += 1
        return True
        
        
    def pop(self) -> Node:
        if self.length == 0: return None
        
        temp = self.tail
        
        if self.length == 1:
            self.head = None
            self.tail = None
            
        else:
            self.tail = temp.prev
            self.tail.next = None
            temp.prev = None
        
        self.length -= 1
        return temp
        
    def prepend(self, value) -> bool:
        new_node = Node(value)
        
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            
        self.length += 1
        return True
            
    def pop_first(self) -> Node:
        if self.head == None:
            return None
        
        temp = self.head
        
        if self.length == 1:
            self.head = None
            self.tail = None
        
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
            
        
        self.length -= 1
        return temp
        
    def get(self, index) -> Node: # could write the same method as SLL, but we can optimize it
        if index < 0 or index >= self.length: return None
        
        temp = self.head
        if index <= self.length/2:
            for _ in range(index):
                temp = temp.next
                
        else:
            temp = self.tail
            # for _ in range(self.length - (index + 1)):
            for _ in range(self.length -1, index, -1):
                temp = temp.prev
                
        return temp
        
    
    def set_value(self, index, value) -> bool:
        temp = self.get(index)
        
        if temp is not None:
            temp.value = value
            return True
        return False
                
                
    def insert(self, index, value) -> bool:
        if index < 0 or index > self.length: return False
        
        if index == 0:
            return self.prepend(value)
        
        if index == self.length:
            return self.append(value)
        
        new_node = Node(value)
        after = self.get(index)
        before = after.prev
        
        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node
         
        self.length += 1
        return True
        
            
    def remove(self, index) -> Node:
        if index < 0 or index >= self.length: return None
        
        if index == 0:
            return self.pop_first()
        
        if index == self.length - 1:
            return self.pop()
        
        current = self.get(index)
        
        if self.length == 1:
            self.head = None
            self.tail = None
            
        else:
            before = current.prev
            after = current.next
            
            before.next = current.next
            after.prev = before
            current.prev = None
            current.next = None 
            
            
        self.length -= 1
        return current
                
                
my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(4)
my_doubly_linked_list.pop()
my_doubly_linked_list.prepend(0)
my_doubly_linked_list.pop_first()
my_doubly_linked_list.append(4)
my_doubly_linked_list.append(5)
# print(my_doubly_linked_list.get(4).value)

my_doubly_linked_list.set_value(3, 44)
my_doubly_linked_list.insert(5, 99)
my_doubly_linked_list.remove(5)

my_doubly_linked_list.print_list()