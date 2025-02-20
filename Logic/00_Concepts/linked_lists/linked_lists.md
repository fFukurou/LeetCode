# Linked Lists

## Do not have indexes, and are spread all over the place, as opposed to a normal list

![alt text](00_Concepts\imgs\image-3.png)

![alt text](00_Concepts\imgs\image-4.png)


## BIG O
### Adding and Removing:
- Appending New Item at the END: O(1)
- Removing an Item at the END: O(n)
- Adding item at the START: O(1) (because the HEAD pointer is already 'one' distance from it)
- Removing item at the START: O(1) (same principle)
- Adding item in the MIDDLE: O(n)
- Removing item from the MIDDLE: O(n)

### Searching elements:
- Searching by value AND index: O(n) (because it has no index, we have to start at the HEAD)

### Reversing:
- Reverse: 

## CHART:
![alt text](00_Concepts\imgs\image-5.png)

## Under the Hood:
![alt text](00_Concepts\imgs\image-6.png)

