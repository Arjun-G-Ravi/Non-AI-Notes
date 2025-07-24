class Node:
    def __init__(self, value, left_child=None, right_child=None):
        self.val = value
        self.left = left_child
        self.right = right_child
    
    def __repr__(self):
        return f'Node({self.val})'

class BST:
    def __init__(self, arr=None):
        self.root = None 
        if arr:
            for i in arr:
                self.insert(i)

    def insert(self, val):
        if not self.root:
            self.root = Node(val)
        else:
            curr = self.root

            while True:
                if val == curr.val:
                    break # no repetition allowed in THIS BST
                if val<curr.val:
                    if curr.left:
                        curr = curr.left
                    else:
                        curr.left = Node(val)
                        break
                elif val>curr.val:
                    if curr.right:
                        curr = curr.right
                    else:
                        curr.right = Node(val)
                        break
    
    def print(self):
        '''Traverse in BFS'''
        frontier = [self.root] # queue
        
        while frontier:
            curr = frontier.pop(0)
            print(curr.val)
            if curr.left:
                frontier.append(curr.left)
            if curr.right:
                frontier.append(curr.right)
    
    def find(self, val):
        curr = self.root
        while True: 
            if val == curr.val: 
                return curr
            if val<curr.val:
                if curr.left:
                    curr = curr.left
                else:
                    return None
            elif val>curr.val:
                if curr.right:
                    curr = curr.right
                else:
                    return None
                
if __name__ == '__main__':
    bst = BST([10, 3, 9, 30, 130, 12, 17, 14, 0, 23, 140, 24, 1, 2])

    bst.print()
    v =  bst.find(12)
    print(v)