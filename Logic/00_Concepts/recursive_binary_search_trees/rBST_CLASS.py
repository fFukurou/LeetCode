class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class rBST:
    def __init__(self):
        self.root = None
        
    
    def __r_contains(self, current_node, value):
        if current_node == None:
            return False
        
        if value == current_node.value:
            return True
    
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
    
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)
        
    
    def r_contains(self, value):
        return self.__r_contains(self.root, value)

    
    def __r_insert(self, current_node, value):
        if current_node == None:
             return Node(value)
         
        if value < current_node.value:
             current_node.left = self.__r_insert(current_node.left, value)
             
        elif value > current_node.value:
             current_node.right = self.__r_insert(current_node.right, value)
             
        return current_node
         
        
    def r_insert(self, value):
        if self.root == None:
            self.root = Node(value)
        
        self.__r_insert(self.root, value)
        
        
    # If deleting a node with a subtree, move the subtree to the position of the deleted node,
    # If deleting a node with two subtrees, pick the lowest value Node from the subtree on the right, copy the value into the node we were supposed to delete, and delete the other node instead.
    def __delete_node(self, current_node, value):
        # current_node is the Node that is being pointed to by the previous iteration
        if current_node == None:
            return None
        
        if value < current_node.value:
            current_node.left = self.__delete_node(current_node.left, value)
            
        elif value > current_node.value:
            current_node.right = self.__delete_node(current_node.right, value)
            
        elif current_node.value == value:
            # If node is a Leaf node
            if current_node.left == None and current_node.right == None:
                return None
            # If node has a Node only on the right
            elif current_node.left == None:
                # So the previous 'current_node' point to this current_node, skipping the value we want to delete, which will be garbage-collected
                current_node = current_node.right
            
            # If node has a Node only on the left
            elif current_node.right == None:
                current_node = current_node.left
                
            # If node has Nodes on both sides
            else:
                # current_node is the Node parent of the before the subtree
                # 1: Find the lowest node in the subtree
                sub_tree_min = self.min_value(current_node.right)
                # 2: replace the value of current_node with the value of the lowest node
                current_node.value = sub_tree_min
                # 3: traverse through the subtree and delete the lowest node
                self.__delete_node(current_node.right, sub_tree_min)
            
        return current_node
    
    
    def delete_node(self, value):
        self.root = self.__delete_node(self.root, value)
        
    # We continuasly go to the left, until we reach None, basically
    def min_value(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
            
        return current_node.value



        
my_tree = rBST()
my_tree.r_insert(47)
my_tree.r_insert(21)
my_tree.r_insert(76)
my_tree.r_insert(18)
my_tree.r_insert(27)
my_tree.r_insert(52)
my_tree.r_insert(82)


print("Root:", my_tree.root.value)
print("Root -> Left:", my_tree.root.left.value)
print("Root -> Right:", my_tree.root.right.value)

print(my_tree.r_contains(99))
print(my_tree.r_contains(27))

print("Minimun node value in the tree:", my_tree.min_value(my_tree.root))
print("Minimun node value in the subtree 76:", my_tree.min_value(my_tree.root.right))

my_tree.delete_node(47)
print("Root:", my_tree.root.value)