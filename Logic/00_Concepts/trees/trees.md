- Is a LinkedList that forks

- Each node points to another 2+ nodes
- (Parents and Childs (Siblings))
- Every node can only have one parent


## FULL:
- Is when a tree only points to ZERO nodes or TWO other nodes
- Meaning a node points to only ONE other node is not FULL

## PERFECT:
- When every level of the tree is perefectly filled, has no gaps


## Complete:
- Filling the tree, with left to right, with no gaps

## LEAF:
- Nodes that do not have ny children



# Binary Search Tree
- If a child is greater than the parent, it goes to the right, if it is lesser, it goes to the left.
- When adding a new node, we always compare to the first parent, and if it doesn't have an open spot, we compare it to the child, and so on.

### If you take any node in the BST, all nodes below it to the right are gonna be greater than that node, and everything to the left will be lesser.


# BIG O:
- Finding, Removing and Adding a node: O(log n) (DIVIDE AND CONQUER)
- (technically it is O(n) if it's a straight line, then it would be a LinkedList, but we treat it as a O(log n) data structure)


