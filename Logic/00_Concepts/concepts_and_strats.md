# DSA

# The 'BIG O' -> O(n)

### O(n) --> 'n' is the number of operations --> Constant
- Is proportional and linear

![alt text](00_Concepts\imgs\image.png)

- Drop constants: It doesn't matter if it's 2n or 3n, simplify if to O(n)

### O(n²)
- Most common is a loop within a loop

- Drop Non-Dominants: O(n² + n) -> the single 'n' is so insignificant that we just drop it

### O(1) -> Constant time
- Most optimal Big O, the number of operations remains constant

### O(log n)  --> Divide and Conquer
- For example, finding a number in an Array: cut the array in half, then again, and again, and then you find it, without having to iterate through the entire array

- 
### O(nlog n) -> Useb by some sorting algorithms


### O(a + b) / O(a * b) -> Different Terms for Inputs

### Big O of lists
#### Adding/Removing elements:
- If no RE-indexing: 1 operation O(1)
- if RE-indexing at the START or MIDDLE: O(n) -> n is the number of elements in the list

#### Searching:
- If searching a VALUE: O(n)
- If searching an INDEX: O(1)


### Final Example:
#### O(100):
- O(1) = 1
- O(log n) =~ 7
- O(n) = 100
- O(n²) = 10000


# POINTERS
 ![alt text](00_Concepts\imgs\image-1.png)

 ![alt text](00_Concepts\imgs\image-2.png)

 ### Integers and Dictionaries work differently
 ## When changing an int variable, it points to another memory location, because integers are imutable
 ## When changing a value in a dict, both values are changed, because they still point to the same space in memory
 ## You can change how dictionaries point at each other
 ## Note: If no variable is pointing to a dictionary, garbage collection needs to be used to remove it from memory
 

