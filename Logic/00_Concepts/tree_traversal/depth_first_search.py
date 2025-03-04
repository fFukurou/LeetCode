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
        
            
    # appends each node as it iterates through the tree
    def DFS_pre_order(self):
        results = []
        
        def traverse(current_node):
            results.append(current_node.value)
            
            if current_node.left is not None:
                traverse(current_node.left)
                
            if current_node.right is not None:
                traverse(current_node.right)
        
        traverse(self.root)
        return results
        
        
    # appends each node after it gets to the bottom left of the tree and checks .left and .right
    def DFS_post_order(self):
        results = []
        
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
                
            if current_node.right is not None:
                traverse(current_node.right)
                
            results.append(current_node.value)
            
        traverse(self.root)
        return results
    
    
    # appends each node after it gets to the bottom left of the three, checks .left, adds to results, then checks .right
    # values get added to the list in ascending order
    def DFS_in_order(self):
        results = []
        
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
                
            results.append(current_node.value)
            
            if current_node.right is not None:
                traverse(current_node.right)
            
        traverse(self.root)
        return results
        
        
        
my_tree = BinarySearchTree()

my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print(my_tree.BFS())
print(my_tree.DFS_pre_order())
print(my_tree.DFS_post_order())
print(my_tree.DFS_in_order())
        