class MaxHeap:
    def __init__(self):
        self.heap = []
        
    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2
    
    def _parent(self, index):
        return (index - 1) // 2
    
    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]
        
        
    # We add the value to the END of the list, and bring it up if necessary
    def insert(self, value): # --> O(log n)
        self.heap.append(value)
        current_index = len(self.heap) - 1
        
        while current_index > 0 and self.heap[current_index] > self.heap[self._parent(current_index)]:
            self._swap(current_index, self._parent(current_index))
            current_index = self._parent(current_index)
            
        
    # Compare a node with its child, if it is lesser than the child, moves it down
    def _sink_down(self, index):
        max_index = index
        
        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)
            
            if left_index < len(self.heap) and self.heap[left_index] > self.heap[max_index]:
                max_index = left_index
                
            if right_index < len(self.heap) and self.heap[right_index] > self.heap[max_index]:
                max_index = right_index
            
            if max_index != index:
                self._swap(index, max_index)
                index = max_index
            else:
                return
            
            
    # We ALWAYS remove the item at the top, get the last item in the heap and sink it down
    def remove(self): # --> O(log n)
        if len(self.heap) == 0:
            return None
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down(0)
        
        return max_value
    
            
            
            
my_heap = MaxHeap()

my_heap.insert(99)
my_heap.insert(72)
my_heap.insert(61)
my_heap.insert(58)

print(my_heap.heap)
my_heap.insert(100)
print(my_heap.heap)
my_heap.insert(75)
print(my_heap.heap)

my_heap.remove()
print(my_heap.heap)
my_heap.remove()
print(my_heap.heap)
