class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

class BinarySearchTree:
    def __init__(self):
        self.root = None
        
        
    def insert(self, value) -> bool:
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
            return True
        
        temp = self.root
        
        while True:
            if temp.value == new_node.value:
                return False
            
            if new_node.value < temp.value:
                if temp.left == None:
                    temp.left = new_node
                    return True
                temp = temp.left
                
            else:
                if temp.right == None:
                    temp.right = new_node
                    return True
                temp = temp.right


                
        
        
    def contains(self, value) -> bool:
        temp = self.root
        
        while temp != None:
            if temp.value == value:
                return True
            
            elif value < temp.value:
                temp = temp.left
                
            elif value > temp.value:
                temp = temp.right
        
        return False
    
    
    
    
my_tree = BinarySearchTree()


my_tree.insert(2)
my_tree.insert(1)
my_tree.insert(3)
my_tree.insert(4)
my_tree.insert(-1)

print(my_tree.contains(19))
# print(my_tree.root.left.right.value)