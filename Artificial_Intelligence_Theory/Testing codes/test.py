
class Node:
    def __init__(self, name, children, val=None):
        self.name = name
        self.val = val
        self.alpha = None
        self.beta = None
        self.children = children
    
    def __repr__(self):
        return f'Node {self.name}:{self.val}, alpha={self.alpha}, beta={self.beta}'

# Terminal states
a = Node('a', None, val=10)
b = Node('b', None, val=3)
c = Node('c', None, val=4)
d = Node('d', None, val=5)
e = Node('e', None, val=2)
f = Node('f', None, val=1)
g = Node('g', None, val=3)
h = Node('h', None, val=5)

# Create Tree
i = Node('i', [a, b])
j = Node('j', [c, d]) 
k = Node('k', [e, f])
l = Node('l', [g, h])
m = Node('m', [i, j])
n = Node('n', [k, l])
root = Node('root', [m, n])
def print_tree_with_alpha_beta(node, is_maximizing, alpha, beta):
    if node is None:
        return
    node.alpha = alpha
    node.beta = beta
    print(node)
    if not node.children:
        return
    
    if is_maximizing:
        for idx, child in enumerate(node.children):
            print_tree_with_alpha_beta(child, False, alpha, beta)
            alpha = max(alpha, child.beta)
            if beta <= alpha:
                print(f"Pruned branch {idx + 1} from {node} onwards")
                break  # Beta pruning
    else:
        for idx, child in enumerate(node.children):
            print_tree_with_alpha_beta(child, True, alpha, beta)
            beta = min(beta, child.alpha)
            if beta <= alpha:
                print(f"Pruned branch {idx + 1} from {node} onwards")
                break  # Alpha pruning

print_tree_with_alpha_beta(root, True, float('-inf'), float('inf'))
