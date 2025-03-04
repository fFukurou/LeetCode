class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

class BinarySearchTree:
    # def __init__(self, value):
        # new_node = Node(value)
        # self.root = new_node
    def __init__(self):
        self.root = None
        
    
    def insert(self, value) -> bool:
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
            return True
            
        temp = self.root
        while True:
            if new_node.value == temp.value: return False
            
            if new_node.value < temp.value:
                if temp.left == None:
                    temp.left = new_node
                    return True
                else:
                    temp = temp.left
                    
            elif new_node.value > temp.value:
                if temp.right == None:
                    temp.right = new_node
                    return True 
                else:
                    temp = temp.right

        
    def contains(self, value) -> bool:
        # if self.root == None: return False
        
        temp = self.root
        
        while temp != None:
            if value == temp.value:
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


print(my_tree.root.value)
print(my_tree.root.left.value)
print(my_tree.root.right.value)
        
print(my_tree.contains(4))
    
        