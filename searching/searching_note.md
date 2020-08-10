# Searching Notes
## Terminalnogy
floor(x): The largest that smaller than or equal to x.
ceiling(x): The smallest that larger than or equal to x.
## Sequential Search(in an unordered linked-list)
Slow for search and insert
## Binary Search(in an ordered array) recursive / iterative
Very slow for insert, fast for search
## Binary Search Tree
1. Combines the flexibility of insertion in a linked-list with the efficiency of search in an ordered array.
2. Use two links per node
3. Key in any node is larger than the keys in all nodes in that node's left subtree and smaller than the keys in all nodes in that node's right subtree
4. The running time of algorithms on binary search trees depend on the shapes of the trees. The best is lgN(balanced), the worst is the N(tree have only one branch)
5. BSTs allow us to keep the keys in order
6. poor worst-case performance
## Balanced Search Tree
2-3 search tree
1. 2-node, with one key(one associated value) and two links(like the nodes in the binary search tree)
2. 3-node, with two keys(two associated values) and three links  
3. perfact balanced 2-3 search tree: all null links are same far from the root 
4. the transformations of 2-3 tree are local, hence every transformation preserves order and the perfect balance in the whole tree.
### Red-Black Balanced Search Tree
#### Rotation
#### color flip
black height increase by 1 whenever root is involved in a color flip

## Hash Tables