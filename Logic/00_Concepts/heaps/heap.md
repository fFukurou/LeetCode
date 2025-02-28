## It is a Binary Tree, but each Node is higher than its descendants
## Highest value will always be at the top
### It is complete (filled from left to right)
## CAN have duplicates
## Can either be a MAX heap or MIN heap
## There is no particular ORDER, except that all the desncendants are gonna have a lower value
### Not good for searching
### Will be represented as as a list, with no Node Class
### Can not have any gaps (perfect)
## Finding Nodes:
### Children:
- Left Children: 2 * parent_index
- Right Children: 2 * parent_index + 1
### Parent:
parent = child_index / 2

# PRIORITY QUEUE
### Highest Value is the highest priority | Always want to remove the highest value

# BIG O
--> O(log n)
