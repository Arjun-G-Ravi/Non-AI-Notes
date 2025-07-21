# Heap tree
A heap is a specialized tree-based data structure that satisfies the heap property. In max heap trees, heap property says that the parent is always greater than the child node. (vice versa for min tree)

`This ensures that for max heap, the root node is the greatest element in the tree. This allows O(1) access to the maximum element.`

### Properties of max heap
- `Structural Property:` It should ALWAYS be an 'Almost Complete Binary Tree' (ACBT). This means that:
  - Left child should be filled before the right
  - Lower layers can be filled only after upper layers are filled
- `Ordering Property:` The heap property is followed
  - Parent > Child: Max heap
  - Child > Parent: Min heap

### Representation as array
- An easy way to represent heaps is to store them in an array. Then, for any element at index `i`(0-based index):
  - Left child is at `2*i + 1`
  - Right child is at `2*i + 2`
  - Parent is at `(i-1)//2`

### For coding in Python
- Create heap as heapq.heapify(list)
- heappop() and heappush() to add and remove
- heap[0] reveals min/max element

### Note
- Heaps form the canonically underlying data stucture for priority queues.
- 