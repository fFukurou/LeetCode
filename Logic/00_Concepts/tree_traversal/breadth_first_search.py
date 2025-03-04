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
        
    # We get the values row by row
    def BFS(self):
        current_node = self.root
        queue = []
        results = []
        queue.append(current_node)
        
        while len(queue) > 0:
            current_node = queue.pop(0)
            results.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
                
        return results
        
            
        
        
        
        
            
my_tree = BinarySearchTree()

my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(376)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)

print(my_tree.BFS())
        