# Heap/ Heap tree
A heap is a specialized tree-based data structure that satisfies the heap property. The heap property can be defined differently based on the type of heap. In max heap trees, the parent is always greater than the child node. (vice versa for min tree)

`This ensures that for max heap, the root node is the greatest element in the tree.`

Properties of max heap
- It should be an 'Almost Complete Binary Tree' (ACBT). This means that:
  - Left child should be filled before the right
  - A layer can be filled only after its upper layer is filled
- The heap property is followed
  - Parent > Child: Max heap
  - Child > Parent: Min heap

Learn creatino, insertion, heapify, deletion, etc. when leetcoding.