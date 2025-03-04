class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else: 
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def dfs_inorder(self):
        results = []
        
        def traverse(current_node):
            if current_node.left != None:
                traverse(current_node.left)
                
            results.append(current_node.value)
            
            if current_node.right != None:
                traverse(current_node.right)
        
        traverse(self.root)
        return results
    
    # WRITE KTH_SMALLEST METHOD HERE #
    def kth_smallest(self, k):
        if self.root == None:
            return None
        
        node_values = self.dfs_inorder()        
        
        if k < 1 or k > len(node_values):
            return None
        
        return node_values[k - 1]
        
    ##################################



bst = BinarySearchTree()

bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(2)
bst.insert(4)
bst.insert(6)
bst.insert(8)

print(bst.kth_smallest(1))  # Expected output: 2
print(bst.kth_smallest(3))  # Expected output: 4
print(bst.kth_smallest(6))  # Expected output: 7


"""
    EXPECTED OUTPUT:
    ----------------
    2
    4
    7

 """