class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size
        
    
    def __hash(self, key): # O(1)
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)
            
            
    
    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        
        # else:
        #     for item in self.data_map[index]:
        #         if item[0] == key: return False
        
        item = [key, value]
        self.data_map[index].append(item)
        return True
        
            
    def get_item(self, key):
        index = self.__hash(key)
        
        if self.data_map[index] != None:
            # for i in range(len(self.data_map[index])):
                # if self.data_map[index][i][0] == key:
                    # return self.data_map[index][i][1]
            
            for item in self.data_map[index]:
                if item[0] == key:
                    return item[1]
        
        return None
        
        
    def get_keys(self):
        all_keys = []
        # for i in range(len(self.data_map)):
            # if self.data_map[i] is not None:
                # for j in range(len(self.data_map[i])):
                    # all_keys.append(self.data_map[i][j][0])
        for slot in self.data_map:
            if slot != None:
                for item in slot:
                    all_keys.append(item[0])
                    
        return all_keys
        
        
        
my_hash_table = HashTable()

my_hash_table.set_item('bolts', 5)
my_hash_table.set_item('washers', 16000)
my_hash_table.set_item('lumber', 34)

my_hash_table.print_table()

print(my_hash_table.get_item('bolts'))
print(my_hash_table.get_item('washers'))
print(my_hash_table.get_item('lumber'))
print(my_hash_table.get_item('bruh'))
print(my_hash_table.get_keys())
