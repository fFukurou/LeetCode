class Graph:
    def __init__(self):
        pass
        
         
    def print_graph(self):
        pass
         
         
    def add_vertex(self, vertex): # ---> O(1)
        pass
        
        
    def add_edge(self, vertex1, vertex2): # ---> O(n)
        pass
        
        
    def remove_edge(self, vertex1, vertex2): # ---> O(|E|)
        pass
                
        
    def remove_vertex(self, vertex): # --> O(|V| + |E|) 
        pass
            
  
my_graph = Graph()
my_graph.add_vertex('A')
my_graph.add_vertex('B')
my_graph.add_vertex('C')

my_graph.add_edge('A', 'B')
my_graph.add_edge('C', 'B')
my_graph.add_edge('A', 'C')

my_graph.remove_edge('A', 'B')
my_graph.remove_edge('A', 'B')

my_graph.remove_vertex('B')

my_graph.print_graph()