binary = [1, 1, 0 , 1]

binary = 1101

binary_num = [int(bit) for bit in str(binary)]

num = 0
for bit in binary_num:
    num = num * 2 + bit
    
    
    
print(num)