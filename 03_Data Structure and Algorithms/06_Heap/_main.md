# Heap tree
A heap is a specialized tree-based data structure that satisfies the heap property. The heap property can be defined differently based on the type of heap. In max heap trees, the parent is always greater than the child node. (vice versa for min tree)

`This ensures that for max heap, the root node is the greatest element in the tree.`

Properties of max heap
- `Structural Property:` It should be an 'Almost Complete Binary Tree' (ACBT). This means that:
  - Left child should be filled before the right
  - Lower layers can be filled only after upper layers are filled
- `Ordering Property:` The heap property is followed
  - Parent > Child: Max heap
  - Child > Parent: Min heap

# For codingm in Python

- Create heap as heapq.heapify(list)
- heappop() and heappush() to add and remove
- heap[0] reveals min/max element
