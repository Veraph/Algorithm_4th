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

