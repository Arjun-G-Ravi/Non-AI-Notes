class Graph:
    def __init__(self, nodes:list):
        self.nodes = {i:[] for i in nodes}
    
    def create_edge(self, node1, node2, weight = None):
        self.nodes[node1].extend([node2, weight])
    
    def print(self):
        for i in self.nodes:
            print(f'{i}: [{self.nodes[i]}]')
            



if __name__ == "__main__":
    g = Graph([1,2,3])
    g.create_edge(1,2,10)
    g.create_edge(3,2,0)
    g.print()

        