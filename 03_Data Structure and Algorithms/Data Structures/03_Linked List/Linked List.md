# Linked List
A linked list consists of a series of nodes, each containing two main components: the data/value that the node holds and a reference (or pointer) to the next node in the sequence. It doesn’t have a fixed length (nodes can be dynamically allocated).
The first node of the linked list is called the "head."

- Insertion is more efficient
- Has to store pointers, though -> more memory compared to arrays

![Alt text](image.png)

## Complexity
- Insertion/ Deletion at head: O(1)
- Insertion/ Deletion: O(n)
- Traversal: O(n)
- Access element by value/index [search]: O(n)

#### Varients
- Doubly linked list: Links to next and previous elements.
- Circular Linked Lists: They do not have ends.

## Tips
- To find middle in O(1) time, use **fast-and-slow pointer technique**