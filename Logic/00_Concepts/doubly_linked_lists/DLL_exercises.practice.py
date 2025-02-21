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
        
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
            
    
    def append(self, value) -> bool:
        new_node = Node(value)
        
        if self.head == None:
            self.head = new_node
            
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
        
        self.tail = new_node
        
        self.length += 1
        return True
        
        
    def pop(self) -> Node:
        if self.head == None: return None
        
        temp = self.tail
        
        if self.length == 1:
            self.tail = None
            self.head = None
        else:
            self.tail = temp.prev
            temp.next = None
            temp.prev = None
            self.tail.next = None
        
        self.length -= 1
        return temp
        
        
    def pop_first(self) -> Node:
        if self.head == None: return None
        
        temp = self.head
        
        if self.length == 1:
            self.head = None
            self.tail = None
            
        else:
            self.head = temp.next
            self.head.prev = None
            temp.next = None
            
        
        self.length -= 1
        return temp
        
        
    def prepend(self, value) -> bool:
        new_node = Node(value)
        
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = self.head.prev
            
        self.length += 1
        return True
        

    def get(self, index) -> Node:
        if index < 0 or index >= self.length: return None
        
        if index < self.length / 2:
            temp = self.head
            for _ in range(index):
                temp = temp.next
                
        else:
            temp = self.tail
            for _ in range(self.length - index - 1):
                temp = temp.prev
        
        return temp
            
        
    def set_value(self, index, value) -> bool:
         
        temp = self.get(index)
        if temp is None: return False
        temp.value = value
        return True
        
        
    def insert(self, index, value) -> bool:
        if index < 0 or index > self.length: return False
        
        if index == 0:
            return self.prepend(value)
        
        if index == self.length:
            return self.append(value)
        
        new_node = Node(value)
        previous = self.get(index - 1)
        current = previous.next
        
        previous.next = new_node
        new_node.prev = previous
        new_node.next = current
        current.prev = new_node
        
        self.length += 1
        return True
        
    
    def remove(self, index) -> Node:
        
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        
        temp = self.get(index)
        if temp is None: return None
        
        previous = temp.prev
        
        previous.next = temp.next
        temp.next.prev = previous
        temp.next = None
        temp.prev = None
        
        self.length -= 1
        return temp
        
            


my_doubly_linked_list = DoublyLinkedList(1)

my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(4)
my_doubly_linked_list.append(5)
# my_doubly_linked_list.append(5)
# my_doubly_linked_list.pop()
# my_doubly_linked_list.pop()
# my_doubly_linked_list.pop()
# my_doubly_linked_list.pop()



# my_doubly_linked_list.prepend(1)
# my_doubly_linked_list.prepend(0)
my_doubly_linked_list.pop_first()
my_doubly_linked_list.pop_first()
my_doubly_linked_list.prepend(0)
my_doubly_linked_list.prepend(1)

# print("GET", my_doubly_linked_list.get(0).value)
my_doubly_linked_list.set_value(4, 999)
my_doubly_linked_list.insert(5, 69)

my_doubly_linked_list.remove(5)





my_doubly_linked_list.print_list()