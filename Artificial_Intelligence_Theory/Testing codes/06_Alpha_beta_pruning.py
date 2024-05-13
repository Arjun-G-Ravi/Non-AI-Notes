class Node:
    def __init__(self, children, val=None):
        self.val = val
        self.alpha = None
        self.beta = None
        self.children = children
    
    def __repr__(self):
        return f'Node:{self.val}'
# Terminal states
a = Node(None,val=10)
b = Node(None,val=3)
c = Node(None,val=4)
d = Node(None,val=5)
e = Node(None,val=2)
f = Node(None,val=1)
g = Node(None,val=3)
h = Node(None,val=5)

# Create Tree
i = Node([a,b])
j = Node([c,d]) 
k = Node([e,f])
l = Node([g,h])
m = Node([i,j])
n = Node([k,l])
root = Node([m,n])

def print_tree(root):
    print('Child:',root )
    if not root.children:
        return
    for child in root.children:
        print_tree(child)
print_tree(root)




























