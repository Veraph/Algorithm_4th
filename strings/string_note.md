# Notes of string
## Which string-sorting algorithm should I use?
algorithm | stable? | inplace? | running time | extra space | sweet spot
---|---|---|---|---|---|
insertion sort for strings | y | y | N~N^2 | 1 | small arrays and arrays in order 
quick sort | n | y | NlogN | logN | general purpose when space is tight 
merge sort | y | n | NlogN | N | general purpose stable sort 
3-way quicksort | n | y | N~NlogN | logN | large numbers of equal keys 
LSD string sort | y | n | NW | N | short fixed-length strings 
MSD string sort | y | n | N~NW | N+WR | random strings 
3-way string quicksort | n | y | N~NWlogR | W+logN | general-purpose, strings with long prefix matches

## Tries
A data structure  
Every node has R(R for alphabet size) links
## R-way trie
### Search in a trie
### Insertion into a trie
Do the search first
### Deletion
### Space
number of links in a trie is between RN and RNw(w is the average key length)

## TST(Ternary Search Tries)
have three links instead of R
### Space
number of links in a TST is between 3N and 3Nwe, hence much more space efficient
### Which String symbol-table implementation should I use?

